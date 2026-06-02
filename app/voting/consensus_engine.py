# app/voting/consensus_engine.py

from collections import defaultdict

from app.voting.provider_reliability import (
    get_weight
)


class ConsensusEngine:

    def determine_winner(
        self,
        votes
    ):

        weighted_scores = defaultdict(
            float
        )

        for vote in votes:

            weight = get_weight(
                vote.provider
            )

            weighted_score = (
                vote.confidence
                * weight
            )

            weighted_scores[
                vote.agent
            ] += weighted_score

        winner = max(
            weighted_scores,
            key=weighted_scores.get
        )

        winner_score = (
            weighted_scores[
                winner
            ]
        )

        total_score = sum(
            weighted_scores.values()
        )

        if total_score > 0:

            final_confidence = (
                winner_score
                / total_score
            )

        else:

            final_confidence = 0.0

        return {

            "winner":
                winner,

            "confidence":
                round(
                    final_confidence,
                    3
                ),

            "weighted_scores":
                dict(
                    weighted_scores
                )
        }