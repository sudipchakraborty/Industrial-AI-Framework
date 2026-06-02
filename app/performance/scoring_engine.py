# app/performance/scoring_engine.py

from collections import defaultdict

from app.performance.reliability_store import (
    load_scores
)


class ScoringEngine:

    def weighted_vote(
        self,
        votes
    ):

        provider_scores = (
            load_scores()
        )

        totals = defaultdict(float)

        for vote in votes:

            weight = (
                provider_scores.get(
                    vote.provider,
                    1.0
                )
            )

            totals[
                vote.agent
            ] += (
                vote.confidence
                * weight
            )

        winner = max(
            totals,
            key=totals.get
        )

        return {
            "winner": winner,
            "score":
            round(
                totals[winner],
                3
            ),
            "all_scores":
            dict(totals)
        }