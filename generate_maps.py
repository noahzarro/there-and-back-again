import json
import requests

token = ""
with open("token.json", "r") as f:
    token = json.load(f)["token"]

def download_map(name, long, lat):
    zoom = 3.67
    url = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/pin-s+c12525({long},{lat})/{long},{lat},{zoom},0/500x500?before_layer=settlement-major-label&access_token={token}".format(long = long, lat = lat, zoom = zoom, token = token)
    img = requests.get(url)
    with open( "static/city_maps/" + name + ".png", "wb") as f:
        f.write(img.content)

def get_coordinates(name):
    url = "https://api.mapbox.com/geocoding/v5/mapbox.places/{name}.json?access_token={token}".format(name=name, token = token)
    res = requests.get(url)
    data = res.json()
    coord = data["features"][0]["geometry"]["coordinates"]
    return coord


routes = {}

with open("static/route.json", "r") as f:
    routes = json.load(f)

for item in routes:
    if item["type"] == "city":
        name = item["name"]
        #coords = get_coordinates(name)
        #download_map(name, coords[0], coords[1])


#missing = ["Kapadokya", "Tokyo", "Хива, Xorazm, Uzbekistan", "Karakol, Issyk-Kul, Kyrgyzstan", "Buan"]
missing = ["Central Asia"]
for name in missing:
    coords = get_coordinates(name)
    download_map(name, coords[0], coords[1])

#coords = get_coordinates("Almaty")
#download_map("Almaty", coords[0], coords[1])

