from typing import TypedDict, List
from langgraph.graph import StateGraph

class FactoryState(TypedDict):
    machine_id: str
    temperature: float
    vibration: float
    current: float
    status: str
    alerts: List[str]
    maintenance_required: bool
    control_action: str

def sensor_agent(state: FactoryState):
    print("\n📡 SENSOR AGENT")
    print(f"Machine: {state['machine_id']}")
    print(f"Temperature: {state['temperature']}")
    return state

def fault_agent(state: FactoryState):
    print("\n🤖 FAULT AGENT")
    alerts = []
    if state["temperature"] > 75:
        alerts.append("🔥 OVERHEATING")
    if state["vibration"] > 4:
        alerts.append("⚠ HIGH VIBRATION")
    if state["current"] > 8:
        alerts.append("⚡ HIGH CURRENT")
    if len(alerts) == 0:
        alerts.append("✅ HEALTHY")
    state["alerts"] = alerts
    print("Alerts:", alerts)
    return state

def maintenance_agent(state: FactoryState):
    print("\n🛠 MAINTENANCE AGENT")
    maintenance_required = False
    if (
        state["temperature"] > 80
        or state["vibration"] > 4.5
    ):
        maintenance_required = True
    state["maintenance_required"] = maintenance_required
    print("Maintenance Required:", maintenance_required)
    return state

def control_agent(state: FactoryState):
    print("\n🎛 CONTROL AGENT")
    action = "NO ACTION"
    if state["temperature"] > 85:
        action = "STOP MACHINE"
    elif state["current"] > 9:
        action = "REDUCE LOAD"
    state["control_action"] = action
    print("Control Action:", action)
    return state

def supervisor_agent(state: FactoryState):
    print("\n🧠 SUPERVISOR AGENT")
    print("\n===== FINAL DECISION =====")
    print("Alerts:")
    for alert in state["alerts"]:
        print("-", alert)
    print("Maintenance:", state["maintenance_required"])
    print("Control:", state["control_action"])
    print("==========================")
    return state

graph = StateGraph(FactoryState)

graph.add_node("sensor", sensor_agent)
graph.add_node("fault", fault_agent)
graph.add_node("maintenance", maintenance_agent)
graph.add_node("control", control_agent)
graph.add_node("supervisor", supervisor_agent)

graph.set_entry_point("sensor")

graph.add_edge("sensor", "fault")
graph.add_edge("fault", "maintenance")
graph.add_edge("maintenance", "control")
graph.add_edge("control", "supervisor")

app = graph.compile()

if __name__ == "__main__":

    initial_state = {
        "machine_id": "M001",
        "temperature": 88,
        "vibration": 4.8,
        "current": 9.2,
        "status": "running",
        "alerts": [],
        "maintenance_required": False,
        "control_action": ""
    }
    result = app.invoke(initial_state)