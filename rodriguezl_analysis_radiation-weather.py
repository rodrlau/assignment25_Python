# This script is an assignment from the Data Steward Program, Module 2.5, University of Vienna.
# It is a simple analysis of weather data using classification, basic statistics and visualisation.
# Programmer: Laura Rodríguez, ORCID 0000-0002-1446-2199
# Date: 2025-12-23

# AI support from chatGPT: 
#   suggest an analysis of the data in file F with columns a,b,c,d 
#   with assignemnt requirements

# Uses libraries (pandas, numpy, matplotlib)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Main Programm
# ------------------------------

# Defines function with parameters
def classify_weather(global_rad, threshold=300):
    # Decision: Classifies weather condition based on global radiation.
    if global_rad > threshold:
        return "Sunny"
    else:
        return "Cloudy"

# Defines function 
def analyze_solar_data(filename):
    # Read Excel file
    data = pd.read_excel(filename)

    # Convert columns to numpy arrays
    time = np.array(data["Time[h]"])
    global_rad = np.array(data["GlobalRadiation[W/m2]"])
    diffuse_rad = np.array(data["DiffusRadiation[W/m2]"])
    temperature = np.array(data["AmbientAirTemperature[C]"])
    humidity = np.array(data["AmbientAirHumidity[%]"])

    # Lists for classified data
    weather_type = []

    # Counters
    sunny_count = 0
    cloudy_count = 0

    # Loop with decision
    for g in global_rad:
        condition = classify_weather(g)
        weather_type.append(condition)

        if condition == "Sunny":
            sunny_count += 1
        else:
            cloudy_count += 1

    # Add classification to DataFrame
    data["WeatherType"] = weather_type

    # Print counts
    print("Number of Sunny hours:", sunny_count)
    print("Number of Cloudy hours:", cloudy_count)
    
    # Basic statistics
    avg_global = np.mean(global_rad)
    max_temp = np.max(temperature)
    min_humidity = np.min(humidity)

    # print Basic statistics
    print("Average Global Radiation:", avg_global)
    print("Maximum Temperature:", max_temp)
    print("Minimum Humidity:", min_humidity)

    # Create plots
    
    # Bar chart for weather classification
    plt.figure(figsize=(5, 4))
    plt.bar(["Sunny", "Cloudy"], [sunny_count, cloudy_count], color=["gold", "gray"])
    plt.xlabel("Weather Type")
    plt.ylabel("Number of Hours")
    plt.title("Sunny vs Cloudy Hours")
    plt.grid(axis="y")
    plt.show()

    # Plot solar Radiation Over Time"
    plt.figure(figsize=(10, 5))
    plt.plot(time, global_rad, label="Global Radiation")
    plt.plot(time, diffuse_rad, label="Diffuse Radiation")
    plt.xlabel("Time [h]")
    plt.ylabel("Radiation [W/m²]")
    plt.title("Solar Radiation Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot temperature vs humidity
    plt.figure(figsize=(6, 5))
    plt.scatter(temperature, humidity, c='orange')
    plt.xlabel("Temperature [°C]")
    plt.ylabel("Humidity [%]")
    plt.title("Temperature vs Humidity")
    plt.grid(True)
    plt.show()
    

    return data


# runs the functions on WeatherData.xlsx and the returned DataFrame is stored in the variable result
result = analyze_solar_data("WeatherData.xlsx")
result.to_excel("processed.xlsx", index=False)
