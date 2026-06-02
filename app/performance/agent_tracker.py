# app/performance/agent_tracker.py

from collections import defaultdict

AGENT_STATS = defaultdict(
    lambda: {
        "success": 0,
        "failure": 0
    }
)


def record_success(agent):

    AGENT_STATS[
        agent
    ]["success"] += 1


def record_failure(agent):

    AGENT_STATS[
        agent
    ]["failure"] += 1