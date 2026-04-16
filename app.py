import streamlit as st
import time
from vehicles import Vehicle
from communication import broadcast_message
import pandas as pd

st.set_page_config(page_title="V2V Communication", layout="wide")

st.title("🚗 Vehicle-to-Vehicle Communication System Simulation")

# ---------- Initialize Vehicles ----------
if "vehicles" not in st.session_state:
    st.session_state.vehicles = [Vehicle(i) for i in range(1, 6)]

vehicles = st.session_state.vehicles

# ---------- Sidebar Controls ----------
st.sidebar.header("📡 Send Alert")

sender_id = st.sidebar.selectbox(
    "Select Sender Vehicle",
    [v.vehicle_id for v in vehicles]
)

alert_msg = st.sidebar.selectbox(
    "Choose Alert Type",
    [
        "⚠️ Accident Ahead",
        "🚦 Traffic Jam",
        "🌧️ Bad Weather",
        "🛑 Sudden Brake",
        "🚧 Road Work Ahead"
    ]
)

if st.sidebar.button("Send Alert"):
    sender = next(v for v in vehicles if v.vehicle_id == sender_id)
    sender.send_message(alert_msg)
    broadcast_message(sender, vehicles)
    st.sidebar.success("Alert Sent to Nearby Vehicles!")

# ---------- Move Vehicles ----------
st.subheader("🚘 Vehicle Movement")

if st.button("Move Vehicles Forward"):
    for v in vehicles:
        v.move()
    st.success("Vehicles Moved!")

# ---------- Display Dashboard ----------
st.subheader("📊 Vehicle Status Dashboard")

data = []
for v in vehicles:
    data.append({
        "Vehicle ID": v.vehicle_id,
        "Position": round(v.position, 2),
        "Speed (km/h)": v.speed,
        "Last Message": v.message
    })

df = pd.DataFrame(data)
st.dataframe(df, width="stretch")

import matplotlib.pyplot as plt

st.subheader("🛣️ Live Road View")

positions = [v.position for v in vehicles]
ids = [v.vehicle_id for v in vehicles]

fig, ax = plt.subplots()

ax.scatter(positions, [1]*len(positions))
for i, txt in enumerate(ids):
    ax.annotate(f"V{txt}", (positions[i], 1.02))

ax.set_yticks([])
ax.set_xlabel("Road Distance")
ax.set_title("Vehicle Positions on Road")

st.pyplot(fig)
st.subheader("⏱️ Real-Time Simulation")

run_sim = st.checkbox("Start Live Simulation")

if run_sim:
    placeholder = st.empty()

    for _ in range(50):   # 50 time steps
        for v in vehicles:
            v.move()

        positions = [v.position for v in vehicles]
        ids = [v.vehicle_id for v in vehicles]

        fig, ax = plt.subplots()
        ax.scatter(positions, [1]*len(positions))
        for i, txt in enumerate(ids):
            ax.annotate(f"V{txt}", (positions[i], 1.02))

        ax.set_yticks([])
        ax.set_xlabel("Road Distance")
        ax.set_title("Live Vehicle Movement")

        placeholder.pyplot(fig)
        time.sleep(0.5)

