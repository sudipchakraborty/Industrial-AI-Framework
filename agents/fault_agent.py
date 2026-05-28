class FaultDetectionAgent:

    def analyze(self, data):

        alerts = []

        # Extract sensor values
        temperature = data["temperature"]

        vibration = data["vibration"]

        current = data["current"]


        # =========================
        # TEMPERATURE FAULT
        # =========================
        if temperature > 75:

            alerts.append("🔥 OVERHEATING DETECTED")


        # =========================
        # VIBRATION FAULT
        # =========================
        if vibration > 4:

            alerts.append("⚠ HIGH VIBRATION DETECTED")


        # =========================
        # CURRENT FAULT
        # =========================
        if current > 8:

            alerts.append("⚡ HIGH CURRENT DETECTED")


        # =========================
        # HEALTHY CONDITION
        # =========================
        if len(alerts) == 0:

            alerts.append("✅ MACHINE HEALTHY")


        return alerts