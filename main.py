import folium
import pandas
from settings import Settings
from random import choice
from map_user import Map_user
from scrape_users import ScrapeUsers as su

s = Settings()

# where the users will be stored
users = []
get_users = su().users_dict

# Add all the users to the list
for user in get_users:
    users.append(Map_user(user))

# Draws out the map
my_map = folium.Map(s.map_location, tiles=s.maptype, zoom_start=s.zoom_start)

# Fills user to map
for user in users:
    user.place_user(my_map)

# Saves the index.html file that updates the map if new users are added or removed
my_map.save("index.html")
