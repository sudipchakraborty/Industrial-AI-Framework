# phase10/voting_metrics.py

from collections import defaultdict


class VotingMetrics:

    def __init__(self):

        self.provider_usage = defaultdict(int)
        self.provider_wins = defaultdict(int)

    def record_vote(self, provider):

        self.provider_usage[provider] += 1

    def record_win(self, provider):

        self.provider_wins[provider] += 1

    def summary(self):

        return {
            "provider_usage": dict(self.provider_usage),
            "provider_wins": dict(self.provider_wins)
        }


metrics = VotingMetrics()