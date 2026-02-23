import streamlit as st
import requests
import pandas as pd
import time

BACKEND_URL = "http://127.0.0.1:5001/api/latest"

st.set_page_config(
    page_title="Smart City IoT Dashboard",
    layout="wide"
)

st.title("🚦 Smart City IoT Analytics Control Dashboard")
st.caption("Real-time Traffic & Air Quality Monitoring System")

# -----------------------------
# Session state for time-series
# -----------------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["timestamp", "avg_speed", "traffic_density", "aqi"]
    )

# -----------------------------
# Fetch backend data
# -----------------------------
def fetch_data():
    try:
        response = requests.get(BACKEND_URL, timeout=2)
        return response.json()
    except:
        return None

data = fetch_data()

if data is None:
    st.error("❌ Backend not reachable. Start Flask backend first.")
    st.stop()

# -----------------------------
# Display KPI cards
# -----------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("🚗 Avg Speed (km/h)", data["avg_speed"])
c2.metric("📊 Traffic Density", data["traffic_density"])
c3.metric("🚦 Congestion", data["congestion"])
c4.metric("🌫️ AQI", data["aqi"])

# -----------------------------
# Threshold-based alerts
# -----------------------------
if data["aqi"] > 200:
    st.error("⚠️ AQI is CRITICAL!")
elif data["aqi"] > 120:
    st.warning("⚠️ AQI is MODERATE")
else:
    st.success("✅ AQI is SAFE")

# -----------------------------
# Update time-series data
# -----------------------------
new_row = {
    "timestamp": data["timestamp"],
    "avg_speed": data["avg_speed"],
    "traffic_density": data["traffic_density"],
    "aqi": data["aqi"]
}

st.session_state.data = pd.concat(
    [st.session_state.data, pd.DataFrame([new_row])],
    ignore_index=True
)

# Keep last 20 records
st.session_state.data = st.session_state.data.tail(20)

# -----------------------------
# Charts
# -----------------------------
st.divider()
st.subheader("📈 Live Analytics")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("### Traffic Density (Bar Chart)")
    st.bar_chart(
        st.session_state.data.set_index("timestamp")["traffic_density"]
    )

with chart_col2:
    st.markdown("### AQI Trend (Line Chart)")
    st.line_chart(
        st.session_state.data.set_index("timestamp")["aqi"]
    )

# -----------------------------
# Auto refresh
# -----------------------------
time.sleep(5)
st.rerun()
