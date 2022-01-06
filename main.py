from map_user import Map_user
import folium
import pandas
from random import choice

use_tile = "stamentoner"
# Draws out the map
my_map = folium.Map([57.107118, 12.2520907], tiles=use_tile, zoom_start=15)
caspar = Map_user({"name": "caspar", "location": [
                  57.107118, 12.2520907], "icon": "caspar.png", "age": 23, "sex": "male"})

# create the user on the map
caspar.splash_user(my_map)

# Saves the index.html file that updates the map if new users are added or removed
my_map.save("index.html")
