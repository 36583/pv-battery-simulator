import streamlit as st
import pandas as pd
from modules.simulation import run_simulation
from modules.plot_utils import plot_energy_flow, plot_summary_bar

# --- Streamlit page setup ---
st.set_page_config(page_title="Energy Storage Simulator", layout="wide")
st.title("PV + Energy Storage Simulation Tool")

# --- Layout with columns instead of sidebar ---
left_col, right_col = st.columns([1, 3])

with left_col:
    st.header("Simulation Settings")
    weather = st.selectbox("Weather Type", ["sunny", "cloudy", "rainy"])
    day_type = st.selectbox("Day Type", ["weekday", "weekend"])
    days = st.slider("Number of Simulation Days", min_value=1, max_value=14, value=3)
    simulate_button = st.button("Run Simulation")

# --- Run simulation when button is clicked ---
if simulate_button:
    st.success(f"Running simulation for: {weather} + {day_type}, {days} day(s)")

    # Call the simulation function
    result_df, summaries = run_simulation(weather, day_type, days=days)

    with right_col:
        # --- Plot energy flow chart ---
        st.subheader("Energy Flow Chart")
        fig1 = plot_energy_flow(result_df, weather, day_type)
        st.pyplot(fig1)

        # --- Display summary metrics ---
        st.subheader("Summary Metrics")
        summary_df = pd.DataFrame.from_dict(summaries, orient='index')
        st.dataframe(summary_df)
        fig2 = plot_summary_bar(summaries)
        st.pyplot(fig2)

        # --- Export CSV download button ---
        csv = summary_df.to_csv().encode("utf-8-sig")
        st.download_button("Download summary.csv", csv, file_name="simulation_summary.csv", mime="text/csv")