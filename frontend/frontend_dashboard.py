import streamlit as st
import pandas as pd
import requests
import random
import time
import plotly.express as px

st.set_page_config(page_title="Smart City IoT Analytics", layout="wide")

# ----------------------------------------------------
# Dashboard Title
# ----------------------------------------------------

st.title("🚦 Smart City IoT Analytics Control Dashboard")
st.caption("Real-time Traffic & Air Quality Monitoring System")

# ----------------------------------------------------
# Backend API
# ----------------------------------------------------

API = "http://127.0.0.1:5001/predict"

def get_data():
    try:
        res = requests.get(API)
        return res.json()
    except:
        return {
            "speed": random.randint(30,60),
            "density": random.randint(50,200),
            "congestion": random.choice(["Low","Medium","High"]),
            "aqi": random.randint(50,150)
        }

data = get_data()

speed = data["speed"]
density = data["density"]
congestion = data["congestion"]
aqi = data["aqi"]

# ----------------------------------------------------
# Metrics Row
# ----------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric("🚗 Avg Speed (km/h)", speed)
col2.metric("📊 Traffic Density", density)
col3.metric("🚦 Congestion", congestion)
col4.metric("🌫 AQI", aqi)

if aqi < 80:
    st.success("AQI is SAFE")
elif aqi < 120:
    st.warning("AQI is MODERATE")
else:
    st.error("AQI is POOR")

st.divider()

# ----------------------------------------------------
# Live Analytics Charts
# ----------------------------------------------------

st.subheader("📊 Live Analytics")

col1,col2 = st.columns(2)

traffic_data = pd.DataFrame({
    "Zone":["A","B","C","D","E"],
    "Density":[150,200,90,70,195]
})

aqi_data = pd.DataFrame({
    "Time":["10AM","11AM","12PM","1PM","2PM","3PM"],
    "AQI":[160,150,100,180,140,70]
})

with col1:
    st.write("Traffic Density Across City Zones")
    fig = px.bar(traffic_data,x="Zone",y="Density",color="Density")
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.write("AQI Trend")
    fig2 = px.line(aqi_data,x="Time",y="AQI",markers=True)
    st.plotly_chart(fig2,use_container_width=True)

# ----------------------------------------------------
# Air Quality semi-circular chart
# ----------------------------------------------------

import plotly.graph_objects as go

st.subheader("🌫 Air Quality Index")

aqi_value = aqi   # use value from backend

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = aqi_value,
    title = {'text': "AQI"},
    gauge = {
        'axis': {'range': [0, 300]},
        'bar': {'color': "white"},
        'steps': [
            {'range': [0, 100], 'color': "green"},
            {'range': [100, 200], 'color': "yellow"},
            {'range': [200, 300], 'color': "red"}
        ],
    }
))

fig.update_layout(
    height=400,
    margin=dict(t=50,b=0,l=0,r=0)
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# City Traffic Monitoring Map (Tirupati)
# ----------------------------------------------------

st.subheader("🗺 City Traffic Monitoring Map - Tirupati")

map_data = pd.DataFrame({
    "lat":[13.6288,13.6300,13.6325,13.6255],
    "lon":[79.4192,79.4205,79.4180,79.4220]
})

st.map(map_data)

st.divider()

# ----------------------------------------------------
# Pollution Heat Zones
# ----------------------------------------------------

st.subheader("🔥 Pollution Heat Zones")

heat_data = pd.DataFrame({
    "Zone":["A","B","C","D","E"],
    "AQI":[120,80,150,60,95]
})

fig4 = px.density_heatmap(heat_data,x="Zone",y="AQI",title="Pollution Heat Zones")
st.plotly_chart(fig4,use_container_width=True)

# ----------------------------------------------------
# Auto Refresh
# ----------------------------------------------------

time.sleep(5)
st.rerun()