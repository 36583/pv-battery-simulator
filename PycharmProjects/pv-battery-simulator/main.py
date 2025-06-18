import matplotlib.pyplot as plt
import pandas as pd

# Try to import Streamlit.  If it fails, we assume the script is
# running outside Streamlit and fall back to plt.show().
try:
    import streamlit as st
    IS_STREAMLIT = True
except ImportError:
    IS_STREAMLIT = False

from modules.simulation import run_simulation, run_batch_simulations, export_summaries_to_csv
from modules.plot_utils import plot_energy_flow, plot_summary_bar

# --- Set simulation parameters ---
weather = "cloudy"
day_type = "weekend"
days = 3

# --- Run simulation ---
result_df, summaries = run_simulation(weather=weather, day_type=day_type, days=days)

# --- Show energy flow chart ---
fig1 = plot_energy_flow(result_df, weather, day_type)
if IS_STREAMLIT:
    st.subheader("Energy Flow Chart")
    st.pyplot(fig1)
else:
    fig1.show()

# --- Show summary bar chart ---
fig2 = plot_summary_bar(summaries)
if IS_STREAMLIT:
    st.subheader("Summary Metrics")
    st.pyplot(fig2)
else:
    fig2.show()

# --- Export summary CSV ---
batch_results, batch_summaries = run_batch_simulations(days=1)
export_summaries_to_csv(batch_summaries, filename="simulation_summary.csv")

if IS_STREAMLIT:
    st.success("Batch simulation summary exported to simulation_summary.csv")
else:
    print("Batch simulation summary has been exported to simulation_summary.csv")
