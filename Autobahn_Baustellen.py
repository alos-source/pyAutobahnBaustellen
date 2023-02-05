import requests
import json
from math import sin, cos, sqrt, atan2, pi

def distance(lat1, lon1, lat2, lon2):
    # convert inputs to Float
    lon1 = float(lon1)
    lon2 = float(lon2)
    lat1 = float(lat1)
    lat2 = float(lat2)
    
    # Convert GPS-Cordinates to Radians
    lat1, lon1 = map(lambda x: x * pi / 180, (lat1, lon1))
    lat2, lon2 = map(lambda x: x * pi / 180, (lat2, lon2))
    
    # Calc distance on a sphere
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    R = 6371  # Radius of earth in km

    distance = R * c
    #print(f"distance: {distance}")
    return distance

def get_construction_sites(highway, reference_point_lat, reference_point_long, radius):
    print(f"Baustellen {highway} im Umkreis {radius}km")
    # URL for german autobahn construction sites
    url = f"https://verkehr.autobahn.de/o/autobahn/{highway}/services/roadworks"
    
    # Send Request to URL
    response = requests.get(url)
    
    # Check Response Status
    if response.status_code == 200:
        # process data in json
        data = response.json()
        
        # extract site data
        construction_sites = data['roadworks']
        
        # Filter sites in radius are reference location
        filtered_construction_sites = []
        for site in construction_sites:
            lat = site['coordinate']['lat']
            long = site['coordinate']['long']
            description = site['description']
            subtitle = site['subtitle']
            
            distance_loc = distance(lat, long, reference_point_lat, reference_point_long)
            
            # add sites to list, if they are within radius
            if distance_loc <= radius:
                filtered_construction_sites.append(site)
                print(f"Latitude: {lat}, Longitude: {long}, Distance: {distance_loc}, Descriptions: {description}, Untertitel: {subtitle}")
                
        return filtered_construction_sites
    else:
        print("Fehler beim Abrufen der Daten")