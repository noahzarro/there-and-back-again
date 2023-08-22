from pathlib import Path
import json

"""
build a route json according to the following rules:
dir 001_cityname
    file 001_imagename
dir 002_cityname_ex
    file 001_imagename_ex

ex marked files/dirs will be marked as extended
do not include _ in cityname
"""

start_directory = Path('static/pics')

route = []

for item in start_directory.iterdir():
    if item.is_dir():
        extended = False
        split_name = item.name.split("_")
        city = split_name[1]
        if item.name.split("_")[-1] == "ex":
            extended = True
        route.append({"type": "city", "name": city, "extended": extended})
        for file in item.iterdir():
            extended = False
            path = "static/pics/" + item.name + "/" + file.name
            if file.name.split("_")[-1].split(".")[0] == "ex":
                extended = True
            route.append({"type": "pic", "path": path, "extended": extended})

with open("static/route.json", "w") as f:
    json.dump(route, f)