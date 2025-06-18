import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_energy_flow(data, weather, day_type):
    """
    Generate a line chart showing hourly PV generation, load, battery SOC, and grid usage.
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot energy-related variables over time
    ax.plot(data["Hour"], data["PV_Generation_kWh"], label="PV Generation", linestyle='--')
    ax.plot(data["Hour"], data["Load_Demand_KWh"], label="Load Demand", linestyle='--')
    ax.plot(data["Hour"], data["SOC_KWh"], label="Battery SOC", linewidth=2)
    ax.plot(data["Hour"], data["Grid_KWh"], label="Grid Usage", linestyle='dotted')

    # Chart formatting
    ax.set_title(f"Energy Flow Simulation - Weather: {weather} | Day: {day_type}")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Energy (kWh)")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()

    return fig


def plot_summary_bar(summary):
    """
    Create a bar chart for summary metrics.
    Supports both single-scenario (flat dict) and multi-scenario (nested dict) inputs.
    """
    if isinstance(summary, dict) and all(isinstance(v, dict) for v in summary.values()):
        # Multi-scenario case: plot one bar group per scenario
        df = pd.DataFrame.from_dict(summary, orient='index')
        fig, ax = plt.subplots(figsize=(14, 6))
        df.plot(kind='bar', ax=ax)
        ax.set_title("Multi-Scenario Summary Comparison")
        ax.set_ylabel("Value")
        ax.grid(axis='y')
        fig.tight_layout()
        return fig
    else:
        # Single-scenario case: plot one bar per metric
        labels = list(summary.keys())
        values = list(summary.values())
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(labels, values, color='orange')

        # Add value labels to each bar
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.1f}", ha='center', va='bottom')

        ax.set_title("Summary Metrics of Storage System")
        ax.grid(axis='y', linestyle='--')
        fig.tight_layout()
        return fig