# app/voting/voting_router.py

import time

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)

from app.voting.provider_votes import (
    ProviderVote
)

from app.voting.consensus_engine import (
    ConsensusEngine
)

from app.voting.voting_metrics import (
    metrics
)


class VotingRouter:

    def __init__(
        self,
        openai_provider,
        gemini_provider,
        groq_provider,
        ollama_provider,
        reflection_agent=None
    ):

        self.providers = [

            openai_provider,
            gemini_provider,
            groq_provider,
            ollama_provider

        ]

        self.reflection_agent = (
            reflection_agent
        )

        self.consensus = (
            ConsensusEngine()
        )

    # =====================================
    # SAFE PROVIDER EXECUTION
    # =====================================

    def _execute_provider(
        self,
        provider,
        query
    ):

        start = time.time()

        try:

            result = provider.classify(
                query
            )

            latency = round(
                time.time() - start,
                3
            )

            result[
                "latency"
            ] = latency

            return result

        except Exception as e:

            latency = round(
                time.time() - start,
                3
            )

            print(
                f"\nProvider Error: {e}"
            )

            return {

                "provider":
                    provider.__class__.__name__,

                "agent":
                    "general",

                "confidence":
                    0.0,

                "reason":
                    str(e),

                "latency":
                    latency
            }

    # =====================================
    # ROUTE
    # =====================================

    def route(
        self,
        query
    ):

        votes = []

        provider_results = []

        with ThreadPoolExecutor(
            max_workers=len(
                self.providers
            )
        ) as executor:

            futures = [

                executor.submit(
                    self._execute_provider,
                    provider,
                    query
                )

                for provider
                in self.providers

            ]

            for future in as_completed(
                futures
            ):

                try:

                    result = future.result(
                        timeout=4
                    )

                    provider_results.append(
                        result
                    )

                except Exception as e:

                    print(
                        f"\nProvider timeout/error: {e}"
                    )

        # =================================
        # BUILD VOTES
        # =================================

        for result in provider_results:

            vote = ProviderVote(

                provider=result[
                    "provider"
                ],

                agent=result[
                    "agent"
                ],

                confidence=result[
                    "confidence"
                ],

                reason=result.get(
                    "reason",
                    ""
                )

            )

            votes.append(
                vote
            )

            metrics.record_vote(
                result[
                    "provider"
                ]
            )

        # =================================
        # SAFETY CHECK
        # =================================

        if not votes:

            return {

                "selected_agent":
                    "general",

                "confidence":
                    0.0,

                "validated":
                    False,

                "votes":
                    [],

                "metrics":
                    metrics.summary(),

                "provider_results":
                    []
            }

        # =================================
        # CONSENSUS
        # =================================

        winner = self.consensus.determine_winner(
            votes
        )

        validated = True

        if self.reflection_agent:

            validated = (
                self.reflection_agent
                .validate(
                    query=query,
                    selected_agent=
                    winner[
                        "winner"
                    ]
                )
            )

        # =================================
        # DEBUG OUTPUT
        # =================================

        print(
            "\nProvider Latencies"
        )

        for result in provider_results:

            print(
                f"{result['provider']} "
                f"-> "
                f"{result['latency']}s"
            )

        return {

            "selected_agent":
                winner[
                    "winner"
                ],

            "confidence":
                winner[
                    "confidence"
                ],

            "validated":
                validated,

            "votes":
                votes,

            "metrics":
                metrics.summary(),

            "provider_results":
                provider_results
        }