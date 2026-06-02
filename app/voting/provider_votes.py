# phase10/provider_votes.py

from dataclasses import dataclass


@dataclass
class ProviderVote:
    provider: str
    agent: str
    confidence: float
    reason: str