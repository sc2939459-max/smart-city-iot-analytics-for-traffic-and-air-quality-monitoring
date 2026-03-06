import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
import time

API = "http://127.0.0.1:5001/data"

st.set_page_config(layout="wide")

st.title("🚦 Smart City IoT Control Center")
st.caption("Real-Time Traffic & Air Quality Monitoring")

# ---------------------------
# Fetch Backend Data
# ---------------------------

try:
    r = requests.get(API)
    data = r.json()
except:
    st.error("Backend not reachable. Start Flask backend.")
    st.stop()

# ---------------------------
# KPI CARDS
# ---------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric("🚗 Avg Speed",data["avg_speed"])
c2.metric("📊 Traffic Density",data["traffic_density"])
c3.metric("🌫 AQI",data["aqi"])
c4.metric("🚦 Congestion",data["congestion"])

# ---------------------------
# TRAFFIC SIGNAL STATUS
# ---------------------------

if data["congestion"] == "HIGH":
    st.error("🔴 Heavy Traffic Detected")
elif data["congestion"] == "MEDIUM":
    st.warning("🟡 Moderate Traffic")
else:
    st.success("🟢 Smooth Traffic")

st.divider()

# ---------------------------
# TRAFFIC ANALYTICS
# ---------------------------

col1,col2 = st.columns(2)

traffic = [random.randint(50,200) for i in range(10)]

df = pd.DataFrame({
"Zone":range(1,11),
"Traffic Density":traffic
})

fig1 = px.bar(df,x="Zone",y="Traffic Density",
title="Traffic Density Across City Zones")

col1.plotly_chart(fig1,use_container_width=True)

aqi = [random.randint(40,180) for i in range(10)]

df2 = pd.DataFrame({
"Time":range(1,11),
"AQI":aqi
})

fig2 = px.line(df2,x="Time",y="AQI",
title="AQI Trend")

col2.plotly_chart(fig2,use_container_width=True)

st.divider()

# ---------------------------
# AQI GAUGE
# ---------------------------

st.subheader("Air Quality Index")

fig = go.Figure(go.Indicator(
mode="gauge+number",
value=data["aqi"],
title={"text":"AQI"},
gauge={
"axis":{"range":[0,300]},
"steps":[
{"range":[0,100],"color":"green"},
{"range":[100,200],"color":"yellow"},
{"range":[200,300],"color":"red"}
]
}
))

st.plotly_chart(fig,use_container_width=True)

st.divider()

# ---------------------------
# CITY TRAFFIC MAP
# ---------------------------

st.subheader("City Traffic Monitoring Map")

map_data = pd.DataFrame({
"lat":[13.0827,13.07,13.09,13.1,13.06],
"lon":[80.2707,80.25,80.28,80.29,80.26],
"traffic":[random.randint(50,200) for i in range(5)]
})

fig_map = px.scatter_mapbox(
map_data,
lat="lat",
lon="lon",
size="traffic",
color="traffic",
zoom=10,
mapbox_style="open-street-map",
title="Traffic Congestion Zones"
)

st.plotly_chart(fig_map,use_container_width=True)

st.divider()

# ---------------------------
# POLLUTION HEATMAP
# ---------------------------

st.subheader("Pollution Heat Zones")

heat = pd.DataFrame({
"Zone":["A","B","C","D","E"],
"AQI":[random.randint(40,180) for i in range(5)]
})

fig3 = px.density_heatmap(heat,x="Zone",y="AQI")

st.plotly_chart(fig3,use_container_width=True)

st.divider()


# ---------------------------
# AUTO REFRESH
# ---------------------------

time.sleep(3)
st.rerun()
