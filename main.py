from map_user import Map_user
import folium
import pandas
from random import choice


caspar = Map_user([57.1021802, 12.2520136], "pic.png", "Caspar Danielsson")

use_tile = "stamentoner"
#Draws out the map
my_map = folium.Map([57.107118, 12.2520907], tiles=use_tile, zoom_start=15)
#Places a marker of one user to the map | Later the script will print all users

# map_user().stick_users() <-- This will fill out the map with all existing users later
folium.Marker(caspar.location,
              popup=caspar.user_popup,
              tooltip="click me",
              icon=caspar.icon
              ).add_to(my_map)
#Saves the index.html file that updates the map if new users are added or removed
my_map.save("index.html")
