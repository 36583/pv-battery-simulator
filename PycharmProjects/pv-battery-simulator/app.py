import streamlit as st
import pandas as pd
from modules.simulation import run_simulation
from modules.plot_utils import plot_energy_flow, plot_summary_bar

# --- Streamlit page setup ---
st.set_page_config(page_title="Energy Storage Simulator", layout="wide")
st.title("PV + Energy Storage Simulation Tool")

# --- Sidebar: user input parameters ---
st.sidebar.header("Simulation Settings")
weather = st.sidebar.selectbox("Weather Type", ["sunny", "cloudy", "rainy"])
day_type = st.sidebar.selectbox("Day Type", ["weekday", "weekend"])
days = st.sidebar.slider("Number of Simulation Days", min_value=1, max_value=14, value=3)

simulate_button = st.sidebar.button("Run Simulation")

# --- Run simulation when button is clicked ---
if simulate_button:
    st.success(f"Running simulation for: {weather} + {day_type}, {days} day(s)")

    # Call the simulation function
    result_df, summaries = run_simulation(weather, day_type, days=days)

    # --- Plot energy flow chart ---
    st.subheader("Energy Flow Chart")
    st.pyplot(plot_energy_flow(result_df, weather, day_type))

    # --- Display summary metrics ---
    st.subheader("Summary Metrics")
    summary_df = pd.DataFrame.from_dict(summaries, orient='index')
    st.dataframe(summary_df)

    # --- Export CSV download button ---
    csv = summary_df.to_csv().encode("utf-8-sig")
    st.download_button("Download summary.csv", csv, file_name="simulation_summary.csv", mime="text/csv")
