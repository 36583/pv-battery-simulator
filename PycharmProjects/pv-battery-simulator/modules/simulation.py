import pandas as pd
from .pv_model import generate_pv_scenario
from .load_model import generate_load_scenario
from .battery_model import simulate_battery
from .summary_utils import calculate_summary

def run_simulation(weather, day_type, days=1):
    """
    Simulate PV + Load + Battery interaction over a number of days.

    Parameters:
        weather (str): 'sunny', 'cloudy', or 'rainy'
        day_type (str): 'weekday' or 'weekend'
        days (int): number of consecutive days to simulate

    Returns:
        result_df (DataFrame): hourly simulation results over all days
        all_summaries (dict): daily summary metrics
    """
    all_data = []
    all_summaries = {}
    soc = 5  # Initial battery SOC in kWh

    for day in range(days):
        hours = range(24)
        global_hours = range(day * 24, (day + 1) * 24)

        # Generate PV and Load profiles for this day
        pv_generation = generate_pv_scenario(weather, hours)
        load_demand = generate_load_scenario(day_type, hours)

        # Create a daily DataFrame
        data = pd.DataFrame({
            "Hour": global_hours,
            "PV_Generation_kWh": pv_generation,
            "Load_Demand_KWh": load_demand
        })

        # Simulate battery behavior and update SOC
        data, soc = simulate_battery(data, soc)

        # Store result and summary
        all_data.append(data)
        summary = calculate_summary(data)
        all_summaries[f"Day{day + 1}"] = summary

    # Concatenate all days' data
    result_df = pd.concat(all_data, ignore_index=True)
    return result_df, all_summaries


def run_batch_simulations(days=1):
    """
    Run simulations for all weather and day type combinations.

    Parameters:
        days (int): number of days to simulate per scenario

    Returns:
        all_results (dict): full DataFrame per scenario
        all_summaries (dict): summary for Day 1 per scenario
    """
    all_results = {}
    all_summaries = {}
    weathers = ["sunny", "cloudy", "rainy"]
    day_types = ["weekday", "weekend"]

    for w in weathers:
        for d in day_types:
            label = f"{w}_{d}"
            result_df, summaries = run_simulation(w, d, days=days)
            all_results[label] = result_df
            all_summaries[label] = summaries["Day1"]  # Take Day 1 only for summary

    return all_results, all_summaries


def export_summaries_to_csv(summary_dict, filename="simulation_summary.csv"):
    """
    Export summary dictionary to a CSV file.

    Parameters:
        summary_dict (dict): summary metrics per scenario
        filename (str): output CSV file name
    """
    df = pd.DataFrame.from_dict(summary_dict, orient="index")
    df.index.name = "Scenario"
    df.to_csv(filename, encoding="utf-8-sig")
