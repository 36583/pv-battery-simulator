import numpy as np

def generate_load_scenario(day_type, hours):
    """
    Generate hourly electricity demand profile based on day type.

    Parameters:
        day_type (str): Either 'weekday' or 'weekend'
        hours (iterable): Hour range (e.g. range(24))

    Returns:
        numpy.ndarray: Array of load demand values (in kWh) per hour
    """
    # Simulate different load curves for weekdays and weekends
    if day_type == "weekday":
        # Weekdays: peak around 8am and 7pm, higher fluctuation
        return 2 + 0.7 * np.sin((np.array(hours) - 8) / 12 * np.pi)
    elif day_type == "weekend":
        # Weekends: flatter curve, peak slightly later in the day
        return 2.3 + 0.4 * np.sin((np.array(hours) - 10) / 12 * np.pi)
    else:
        raise ValueError("Unknown day type")
