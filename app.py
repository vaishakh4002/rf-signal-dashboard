# RF Signal Quality Analyzer Dashboard
# Built by: [Your Name] | ECE Graduate Project

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ── PAGE SETUP ──────────────────────────────────────────
st.set_page_config(page_title="RF Signal Analyzer", layout="wide")
st.title("📡 RF Signal Quality Analyzer")
st.markdown("Real-time antenna signal monitoring dashboard")

# ── LOAD DATA ───────────────────────────────────────────
df = pd.read_csv("signal_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# ── SIDEBAR FILTERS ─────────────────────────────────────
st.sidebar.header("Filters")
towers = st.sidebar.multiselect(
    "Select Tower",
    options=df["tower_id"].unique(),
    default=df["tower_id"].unique()
)
df = df[df["tower_id"].isin(towers)]

# ── SUMMARY CARDS ───────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Best Signal (RSSI)", f"{df['RSSI_dBm'].max()} dBm")
col2.metric("Worst Signal (RSSI)", f"{df['RSSI_dBm'].min()} dBm")
col3.metric("Average SNR", f"{round(df['SNR_dB'].mean(), 1)} dB")
col4.metric("Total Readings", len(df))

st.markdown("---")

# ── CHART 1: RSSI over time ──────────────────────────────
st.subheader("Signal Strength (RSSI) Over Time")
fig1, ax1 = plt.subplots(figsize=(10, 4))
for tower in df["tower_id"].unique():
    tower_data = df[df["tower_id"] == tower]
    ax1.plot(tower_data["timestamp"], tower_data["RSSI_dBm"],
             marker="o", label=tower)
ax1.set_xlabel("Time")
ax1.set_ylabel("RSSI (dBm)")
ax1.legend()
ax1.grid(True)
ax1.axhline(y=-85, color="red", linestyle="--", label="Critical Threshold")
st.pyplot(fig1)

# ── CHART 2: SNR over time ───────────────────────────────
st.subheader("Signal-to-Noise Ratio (SNR) Over Time")
fig2, ax2 = plt.subplots(figsize=(10, 4))
for tower in df["tower_id"].unique():
    tower_data = df[df["tower_id"] == tower]
    ax2.plot(tower_data["timestamp"], tower_data["SNR_dB"],
             marker="s", label=tower)
ax2.set_xlabel("Time")
ax2.set_ylabel("SNR (dB)")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

# ── FAULT ALERTS ─────────────────────────────────────────
st.subheader("⚠️ Fault Alerts")
faults = df[df["RSSI_dBm"] < -85]
if len(faults) == 0:
    st.success("All towers operating normally.")
else:
    st.error(f"{len(faults)} fault(s) detected!")
    st.dataframe(faults[["timestamp", "tower_id", "RSSI_dBm", "SNR_dB"]])

# ── RAW DATA TABLE ────────────────────────────────────────
st.subheader("Raw Signal Data")
st.dataframe(df)