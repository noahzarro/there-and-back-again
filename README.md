# There and back again
A template to generate an image only blog, separated into geographical groups.

## Concept
The base for the blog is a folder structure inside the `static/pics` folder. It consists of folders named `<prefix>_cityname[_ex]`. E.g: `010_Bucharest_ex` or `007_Vienna`. The prefix can be used for sorting, and the optional `_ex` postfix has currently no use but may be used in the future to create a different (i.e. extended) version of the blog.

The folders contain photos of this location.

Example:
```
> static
  > pics
    > 000_Zürich
      > 001.jpg
      > 002.png
      > 010.gif
    > 001_Seoul
      > spam.jpg
```
The folder and files are then used to create blog like this:

![Screenshot](screenshot.PNG)

Cities and pictures are shown in alphabetical order. Non alphanumerical characters might be sorted differently then the OS file explorer does.

## Usage

### Folder Structure
First setup the folder structure as described above.

### Generate `route.json`
The `route.json` lists all folders and photos from the file system. It can be created by executing `python generate_route.py` in the main folder.

### Generate Maps
The map images can either be generated manually and stored in the folder `static/city_maps` or generated by executing `python generate_maps.py` in the main folder.

For automatic generation an API token from mapbox.com is needed. It has to be stored in a file `token.json` in the main folder. The file must have the following content: `{"token":"<token>"}`.

It will look up coordinates for all the city names in `route.json` (countries are also possible) and chose the best match. It then generates map snippets with a marker for the specific map. The map images are then placed inside `static/city_maps`.

### Running
The actual web server can be started by executing `python main.py` in the main folder.

### Docker
A docker container can be build via `docker build -t `