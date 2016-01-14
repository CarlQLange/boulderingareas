import requests
from bs4 import BeautifulSoup
import csv

def gridtogps (gridref):
    r = requests.get("http://batlab.ucd.ie/gridref/?reftype=NATGRID&refs=" + gridref)
    xml = r.text

    soup = BeautifulSoup(xml, 'xml')

    pm = soup.gridref.placemark
    lat = pm.latitude.text
    lon = pm.longitude.text

    return {
        'Latitude': lat,
        'Longitude': lon
    }

with open('./areas.csv') as f:
    d = csv.DictReader(f)
    for row in d:
        if (row['OS Map Coordinates']):
            ll = gridtogps(row['OS Map Coordinates'].replace(' ', ''))
            print ','.join([row['Area Name'],row['Number of Problems'],row['Type of Rock'],row['Aspect'],row['County'],row['OS Map Coordinates'],ll['Latitude'],ll['Longitude']])
        else:
            print ','.join([row['Area Name'],row['Number of Problems'],row['Type of Rock'],row['Aspect'],row['County'],row['OS Map Coordinates'],row['Latitude'],row['Longitude']])
