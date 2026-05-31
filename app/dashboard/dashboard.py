import sys
import os

# Add project root path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

import streamlit as st

from streamlit_autorefresh import st_autorefresh

from database.db import get_latest_data


# ======================================
# AUTO REFRESH
# ======================================
st_autorefresh(
    interval=2000,
    key="factorydashboard"
)


# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="Industrial AI System",
    layout="wide"
)


# ======================================
# TITLE
# ======================================
st.title("🏭 Multi-Agent Industrial Automation System")


# ======================================
# FETCH LATEST DATABASE DATA
# ======================================
data = get_latest_data()


if data:

    machine_id, temperature, vibration, current, status = data

else:

    machine_id = "N/A"

    temperature = 0

    vibration = 0

    current = 0

    status = "unknown"


# ======================================
# LIVE MACHINE MONITORING
# ======================================
st.subheader("📡 Live Machine Monitoring")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "🌡 Temperature",
        f"{temperature} °C"
    )


with col2:

    st.metric(
        "📈 Vibration",
        vibration
    )


with col3:

    st.metric(
        "⚡ Current",
        f"{current} A"
    )


# ======================================
# MACHINE STATUS
# ======================================
st.subheader("🟢 Machine Status")


st.write(f"Machine ID: {machine_id}")

st.write(f"Status: {status}")


# ======================================
# AI ALERTS
# ======================================
st.subheader("🚨 AI Fault Alerts")


alerts = []


if temperature > 75:

    alerts.append("🔥 OVERHEATING DETECTED")


if vibration > 4:

    alerts.append("⚠ HIGH VIBRATION DETECTED")


if current > 8:

    alerts.append("⚡ HIGH CURRENT DETECTED")


if len(alerts) == 0:

    alerts.append("✅ MACHINE HEALTHY")


for alert in alerts:

    if "HEALTHY" in alert:

        st.success(alert)

    else:

        st.error(alert)