import numpy as np

def generate_pv_scenario(weather, hours):
    """
    Generate hourly PV generation profile based on weather conditions.

    Parameters:
        weather (str): Weather type - 'sunny', 'cloudy', or 'rainy'
        hours (iterable): Hour range (e.g. range(24))

    Returns:
        numpy.ndarray: Array of PV generation values (in kWh) per hour
    """
    # Use a sine curve to simulate daytime PV generation
    if weather == "sunny":
        return np.maximum(0, np.sin((np.array(hours) - 6) / 12 * np.pi)) * 5
    elif weather == "cloudy":
        return np.maximum(0, np.sin((np.array(hours) - 6) / 12 * np.pi)) * 3
    elif weather == "rainy":
        return np.maximum(0, np.sin((np.array(hours) - 6) / 12 * np.pi)) * 1.5
    else:
        raise ValueError("Unknown weather type")
