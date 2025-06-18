import matplotlib.pyplot as plt
import pandas as pd

def plot_energy_flow(data, weather, day_type):
    """
    Plot hourly energy flow: PV generation, load demand, battery SOC, and grid usage.

    Parameters:
        data (DataFrame): Simulation results with energy values per hour
        weather (str): Weather type (e.g., 'sunny', 'cloudy', 'rainy')
        day_type (str): Day type (e.g., 'weekday', 'weekend')
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data["Hour"], data["PV_Generation_kWh"], label="PV Generation", linestyle='--')
    plt.plot(data["Hour"], data["Load_Demand_KWh"], label="Load Demand", linestyle='--')
    plt.plot(data["Hour"], data["SOC_KWh"], label="Battery SOC", linewidth=2)
    plt.plot(data["Hour"], data["Grid_KWh"], label="Grid Usage", linestyle='dotted')

    plt.title(f"Energy Flow Simulation - Weather: {weather} | Day: {day_type}")
    plt.xlabel("Hour")
    plt.ylabel("Energy (kWh)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_summary_bar(summary):
    """
    Plot a bar chart of summary metrics.
    Can handle both single-day (dict) and multi-scenario (nested dict) summaries.

    Parameters:
        summary (dict): Either a flat dict (single scenario) or nested dict (batch results)
    """
    import numpy as np

    if isinstance(summary, dict) and all(isinstance(v, dict) for v in summary.values()):
        # Multi-scenario bar chart
        df = pd.DataFrame.from_dict(summary, orient='index')
        df.plot(kind='bar', figsize=(14, 6))
        plt.title("Multi-Scenario Summary Comparison")
        plt.xticks(rotation=15)
        plt.ylabel("Value")
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
    else:
        # Single-scenario bar chart
        labels = list(summary.keys())
        values = list(summary.values())
        plt.figure(figsize=(10, 6))
        bars = plt.bar(labels, values, color='orange')

        # Annotate bar values
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height}", ha='center', va='bottom')

        plt.title("Summary Metrics of Storage System")
        plt.xticks(rotation=15)
        plt.grid(axis='y', linestyle='--')
        plt.tight_layout()
        plt.show()
