def simulate_battery(data, initial_soc):
    battery_capacity = 10
    charge_efficiency = 0.95
    discharge_efficiency = 0.9
    min_soc = battery_capacity * 0.1

    soc = [initial_soc]
    charge = []
    discharge = []
    grid_usage = []

    for i in range(24):
        pv = data.loc[i, "PV_Generation_kWh"]
        load = data.loc[i, "Load_Demand_KWh"]
        current_soc = soc[-1]

        charge_kwh = 0
        discharge_kwh = 0
        grid_kwh = 0

        if pv > load:
            surplus = pv - load
            charge_possible = min(surplus * charge_efficiency, battery_capacity - current_soc)
            charge_kwh = charge_possible
            current_soc += charge_kwh
        else:
            deficit = load - pv
            available_discharge = max(current_soc - min_soc, 0)
            discharge_kwh = min(deficit / discharge_efficiency, available_discharge)
            current_soc -= discharge_kwh
            grid_kwh = deficit - discharge_kwh * discharge_efficiency

        soc.append(current_soc)
        charge.append(charge_kwh)
        discharge.append(discharge_kwh)
        grid_usage.append(grid_kwh)

    data["Charge_KWh"] = charge
    data["Discharge_KWh"] = discharge
    data["SOC_KWh"] = soc[1:]
    data["Grid_KWh"] = grid_usage

    return data, soc[-1]
