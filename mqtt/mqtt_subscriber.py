import paho.mqtt.client as mqtt
import json
from agents.fault_agent import FaultDetectionAgent
from database.db import insert_data
###########################################
BROKER = "localhost"
PORT = 1883
TOPIC = "factory/machine1/data"
fault_agent = FaultDetectionAgent()

# ======================================
# MQTT CONNECT CALLBACK
# ======================================
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)
    print(f"Subscribed to: {TOPIC}")

# ======================================
# MQTT MESSAGE CALLBACK
# ======================================
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        print("\n===== SENSOR DATA RECEIVED =====")
        print(f"Machine ID   : {data['machine_id']}")
        print(f"Temperature  : {data['temperature']} °C")
        print(f"Vibration    : {data['vibration']}")
        print(f"Current      : {data['current']} A")
        print(f"Status       : {data['status']}")
        print("================================")

        # ======================================
        # AI FAULT ANALYSIS
        # ======================================
        alerts = fault_agent.analyze(data)
        print("\n===== AI FAULT ANALYSIS =====")
        for alert in alerts:
            print(alert)
        print("=============================")

        # ======================================
        # INSERT INTO SQLITE DATABASE
        # ======================================
        insert_data(
            data["machine_id"],
            data["temperature"],
            data["vibration"],
            data["current"],
            data["status"]
        )
        print("✅ Data inserted into database")

    except Exception as e:
        print("Error:", e)

# ======================================
# MQTT CLIENT
# ======================================
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION1
)
client.on_connect = on_connect
client.on_message = on_message
print("Connecting to MQTT broker...")
client.connect(BROKER, PORT, 60)
client.loop_forever()