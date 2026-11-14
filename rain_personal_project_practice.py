# Practice File for the concepts around getting the rainfall data of Kent (2000-2025) and mapping the rain patterns 
# This file uses VisualCrossing, but its API key has a free account limit for data, so I'm thinking about changing where I get the data.

import urllib.request
import json
import calendar

# Gets JSON precipitation data of a specified coordinate for 1 day using VisualCrossing
def get_data(lat, lon, day):
    coord = str(lat) + ',' + str(lon) 
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + \
    coord + '/' + day + '/' + day + '?unitGroup=metric&elements=precip' + \
  '&key=TL9TEK5P46RHTMHK89PPP8L4M&contentType=json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data

# Tests the start and end dates I'm considering analyzing
# might not work if VisualCrossing API limit is reached
start_date_data = get_data(47.38, -122.23, '2000-01-01')
print(start_date_data)
print("The amount of Precipitation in Kent during January 1st, 2000 is:", start_date_data['days'][0]['precip'], "mm")

end_date_data = get_data(47.38, -122.23, '2025-12-31')
print("The amount of Precipitation in Kent during December 31st, 2025 is:", end_date_data['days'][0]['precip'], "mm")


# Measures average rain in Kent over 1 month 
calend = calendar.Calendar()
sum = 0
days = 0
for days in calend.itermonthdates(2000, 1):
    if days.month == 1:
        this_day = str(days)
        current_date = get_data(47.38, -122.23, this_day)
        sum += current_date['days'][0]['precip']
        days += 1
print("The amount of Precipitaiton in Kent in the month of January 2000 was: ", sum / days, "mm")
