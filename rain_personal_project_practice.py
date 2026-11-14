import urllib.request
import json

# Gets JSON precipitation data of a specified coordinate for 1 day using VisualCrossing
def get_data(lat, lon, day):
    coord = str(lat) + ',' + str(lon) 
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + \
    coord + '/' + day + '/' + day + '?unitGroup=metric&elements=precip' + \
  '&key=TL9TEK5P46RHTMHK89PPP8L4M&contentType=json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data

start_date_data = get_data(47.38, -122.23, '2000-01-01')
print(start_date_data)
print("The amount of Precipitation in Kent during January 1st, 2000 is:", start_date_data['days'][0]['precip'], "mm")

end_date_data = get_data(47.38, -122.23, '2025-12-31')
print("The amount of Precipitation in Kent during December 31st, 2025 is:", end_date_data['days'][0]['precip'], "mm")

