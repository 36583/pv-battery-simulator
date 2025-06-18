from modules.simulation import run_simulation, run_batch_simulations, export_summaries_to_csv
from modules.plot_utils import plot_energy_flow, plot_summary_bar

# --- Set simulation parameters ---
weather = "cloudy"
day_type = "weekend"
days = 3  # Number of days to simulate

# --- Run single-scenario simulation ---
result_df, summaries = run_simulation(weather=weather, day_type=day_type, days=days)

# Plot energy flow and battery behavior
plot_energy_flow(result_df, weather, day_type)

# Plot summary metrics bar chart
plot_summary_bar(summaries)

# --- Run batch simulation for all scenarios ---
batch_results, batch_summaries = run_batch_simulations(days=1)

# Export summary metrics to CSV
export_summaries_to_csv(batch_summaries, filename="simulation_summary.csv")

print("✅ Batch simulation summary has been exported to simulation_summary.csv")
