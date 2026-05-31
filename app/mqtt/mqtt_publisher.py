import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "factory/machine1/data"

# client = mqtt.Client()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(BROKER, PORT, 60)

while True:

    data = {
        "machine_id": "M001",
        "temperature": round(random.uniform(30, 90), 2),
        "vibration": round(random.uniform(0.1, 5.0), 2),
        "current": round(random.uniform(1, 10), 2),
        "status": "running"
    }

    payload = json.dumps(data)

    client.publish(TOPIC, payload)

    print("Published:", payload)

    time.sleep(3)