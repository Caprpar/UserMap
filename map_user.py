import folium


class Map_user:
    """A class tha maps out the user on the map with its info and settings"""

    def __init__(self, user_values):
        self.user_values = user_values
        self.icon = folium.features.CustomIcon(icon_image=self.user_values["icon"],
                                               icon_size=(50, 50))

    def splash_user(self, map):
        user = self.user_values
        folium.Marker(location=user["location"],
                      popup=f"age: {user['age']}\nsex: {user['sex']}",
                      tooltip=user["name"],
                      icon=self.icon).add_to(map)
