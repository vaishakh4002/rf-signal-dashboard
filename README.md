# 📡 RF Signal Quality Analyzer Dashboard

A Python web dashboard to monitor RF antenna signal quality in real time.

## What it does
- Reads antenna signal data (RSSI, SNR, Frequency)
- Displays live charts for signal strength across 3 towers
- Detects faults when signal drops below -85 dBm threshold
- Interactive sidebar to filter by tower

## Tech Stack
- Python 3.14
- Streamlit — web dashboard
- Pandas — data processing
- Matplotlib — charts

## How to run
pip install streamlit pandas matplotlib
python -m streamlit run app.py

## Screenshots
![Dashboard](screenshot1.png)
![Charts](screenshot2.png)
![Fault Alerts](screenshot3.png)

## About
Built as part of ECE to IT transition portfolio.
Domain knowledge applied: RF signal propagation, RSSI and SNR
metrics from antenna design background.