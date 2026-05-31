# app/observability/metrics.py

METRICS = {

    "rule_router_hits": 0,

    "embedding_router_hits": 0,

    "llm_router_hits": 0,

    "reflection_corrections": 0,

    "home_agent_calls": 0,

    "office_agent_calls": 0,

    "doctor_agent_calls": 0,

    "travel_agent_calls": 0,

    "general_agent_calls": 0
}


def increment(metric_name):

    if metric_name in METRICS:
        METRICS[metric_name] += 1


def get_metrics():

    return METRICS
