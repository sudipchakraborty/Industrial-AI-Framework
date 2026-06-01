# app/observability/metrics.py

METRICS = {

    "rule_router_hits": 0,
    "embedding_router_hits": 0,
    "llm_router_hits": 0,

    "approval_requests": 0,
    "approval_approved": 0,
    "approval_rejected": 0,

    "tool_calls": 0,
    "tool_failures": 0,

    "planner_calls": 0,

    "memory_updates": 0,

    "travel_agent_calls": 0,
    "finance_agent_calls": 0,
    "calendar_agent_calls": 0,
    "email_agent_calls": 0
}


def increment(metric_name):

    if metric_name in METRICS:
        METRICS[metric_name] += 1


def get_metrics():

    return METRICS
