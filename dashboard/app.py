import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Load model
model = pickle.load(open("models/traffic_model.pkl", "rb"))

# Load dataset
df = pd.read_csv("data/traffic.csv")

df['date_time'] = pd.to_datetime(df['date_time'], dayfirst=True)
df['hour'] = df['date_time'].dt.hour

# -----------------------------
# PAGE TITLE
# -----------------------------

st.title("🚦 Smart Traffic Prediction System")

st.write("AI system that predicts traffic congestion using machine learning.")

st.subheader("Model Performance")

st.write("""
Model used: Random Forest Regressor  
Features used: Hour, Day, Month, Temperature  
""")

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------

st.sidebar.header("Traffic Prediction Inputs")

day = st.sidebar.slider("Day of Week", 0, 6)
month = st.sidebar.slider("Month", 1, 12)
temp = st.sidebar.slider("Temperature", -10, 40, 20)

# -----------------------------
# TRAFFIC FORECAST GRAPH
# -----------------------------

st.subheader("Predicted Traffic Across 24 Hours")

hours = list(range(24))
predictions = []

for h in hours:
    features = np.array([[h, day, month, temp]])
    pred = model.predict(features)
    predictions.append(pred[0])

fig, ax = plt.subplots()

ax.plot(hours, predictions, marker="o")

ax.set_xlabel("Hour of Day")
ax.set_ylabel("Predicted Traffic Volume")
ax.set_title("Traffic Forecast")

st.pyplot(fig)

# -----------------------------
# TRAFFIC HEATMAP
# -----------------------------
st.subheader("Traffic Congestion Heatmap")

m = folium.Map(location=[40.71, -74.00], zoom_start=12)

traffic_data = [
    [40.7128, -74.0060, 0.9],
    [40.7328, -74.0160, 0.8],
    [40.7428, -74.0260, 0.7],
    [40.7228, -74.0360, 0.85],
    [40.7028, -73.9960, 0.6],
    [40.6928, -74.0460, 0.75],
    [40.7528, -74.0560, 0.9],
    [40.7628, -74.0360, 0.65],
    [40.7728, -74.0160, 0.8],
]

HeatMap(
    traffic_data,
    radius=20,
    blur=15,
    max_zoom=13
).add_to(m)

st_folium(m, width=700, height=500)