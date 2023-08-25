from pathlib import Path
import os
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

start_directory = 'static/pics'

route = []

for dir_name in sorted(os.listdir(start_directory)):
    if os.path.isdir(os.path.join(start_directory, dir_name)):
        extended = False
        print(dir_name)
        split_name = dir_name.split("_")
        city = split_name[1]
        if split_name[-1] == "ex":
            extended = True
        route.append({"type": "city", "name": city, "extended": extended})
        files = os.listdir(os.path.join(start_directory, dir_name))
        sorted_files = sorted(files, key=lambda name: name.lower())
        for file_name in sorted_files:
            extended = False
            path = os.path.join(start_directory, dir_name, file_name)
            print(file_name)
            if file_name.split("_")[-1].split(".")[0] == "ex":
                extended = True
            route.append({"type": "pic", "path": path, "extended": extended})

with open("static/route.json", "w") as f:
    json.dump(route, f)

exit(0)
di = os.listdir(os.path.join(start_directory, "012_Dubrovnik"))
print(di)
so = sorted(di, reverse=True)
print(so)