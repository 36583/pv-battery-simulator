def calculate_summary(data):
    """
    Calculate key performance metrics from the simulation result.

    Parameters:
        data (DataFrame): Simulation result containing hourly PV, load, battery, grid info

    Returns:
        dict: Summary metrics including energy generation, consumption, DOD, self-sufficiency
    """
    battery_capacity = 10  # in kWh (assumed fixed for all scenarios)

    return {
        "Total PV Generation (kWh)": round(data["PV_Generation_kWh"].sum(), 2),
        "Total Load Consumption (kWh)": round(data["Load_Demand_KWh"].sum(), 2),
        "Total Grid Import (kWh)": round(data["Grid_KWh"].sum(), 2),
        "Total Battery Discharge (kWh)": round(data["Discharge_KWh"].sum(), 2),
        "Self-Sufficiency (%)": round(
            100 * (1 - data["Grid_KWh"].sum() / data["Load_Demand_KWh"].sum()), 2
        ),
        "Max Depth of Discharge (DOD %)": round(
            100 * (1 - min(data["SOC_KWh"]) / battery_capacity), 2
        ),
        "Total Battery Throughput (kWh)": round(
            data["Charge_KWh"].sum() + data["Discharge_KWh"].sum(), 2
        )
    }
