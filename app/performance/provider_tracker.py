# app/performance/provider_tracker.py

from app.performance.reliability_store import (
    load_scores,
    save_scores
)


def reward_provider(provider):

    scores = load_scores()

    scores[provider] += 0.01

    save_scores(scores)


def penalize_provider(provider):

    scores = load_scores()

    scores[provider] -= 0.01

    if scores[provider] < 0.1:

        scores[provider] = 0.1

    save_scores(scores)