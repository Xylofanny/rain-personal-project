import requests
import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Switching to Open Meteo API as they are free and give past data from the year 2000
def get_data(url, parameters):
    response = requests.get(url, params=parameters)
    data = response.json()
    return data

# Defining variables and parameters
url = "https://archive-api.open-meteo.com/v1/archive"
parameters = {
    "latitude": 47.38,
    "longitude": -122.23,
    "start_date": "2000-01-01",
    "end_date": "2025-12-31",
    "daily": "precipitation_sum",
    "precipitation_unit": "mm",
}

data = get_data(url, parameters)

# Puts data into dataframe
df_range = pd.DataFrame({
    "date": pd.to_datetime(data["daily"]["time"]),
    "precip_mm": data["daily"]["precipitation_sum"],
})

print("The first five days from 2000-2025 are", df_range.head())

rain_sum = df_range['precip_mm'].sum()
total_days = len(df_range)

print("The average daily amount of Precipitation in Kent from 2000-2025 was:", rain_sum / total_days, "mm")

# Calculating the 26 years in the range
years = []
precipitation = []

# Range's stop value is exclusive so loop ends at 2025
for year in range(2000, 2026):
    parameters["start_date"] = str(year) + "-01-01"
    parameters["end_date"] = str(year) + "-12-31"
    data = get_data(url, parameters)
    years.append(year)
    if calendar.isleap(year):
        precipitation.append(pd.Series(data["daily"]["precipitation_sum"]).sum() / 366)
    else:
        precipitation.append(pd.Series(data["daily"]["precipitation_sum"]).sum() / 365)

df_yearly = pd.DataFrame({
    "year": years,
    "precip_mm": precipitation 
})
df_yearly = df_yearly.set_index("year")
print(df_yearly)

# Putting the years into a line chart
plt.plot(years, precipitation)
plt.ylim(bottom=0)

plt.xlabel("Year")
plt.ylabel("Average daily precipitation in mm")
plt.title("Trend of daily precipitation in Kent, WA")

# Figure appears to show a very slight upward trend of rain, but needs further testing
plt.show()