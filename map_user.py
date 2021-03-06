import folium
from settings import Settings
from branca.element import IFrame


class Map_user:
    """A class tha maps out the user on the map with its info and settings"""

    def __init__(self, user_values):
        """Contains all the user values in a dictionary type"""
        s = Settings()
        self.user_values = user_values  # This is a dictionary
        self.tooltip = user_values['name'].capitalize()
        self.location = self._convertLocation(user_values['location'])
        self.icon = f"{self.user_values['name']}.png"
        self.icon_path = f"avatars/{self.icon}"
        self.age = self.user_values["age"]
        self.sex = self.user_values["sex"]

        # options for the popup bubble
        popup_text = f"Age: {self.age}<br>Sex: {self.sex}"
        iframe = folium.IFrame(popup_text)
        self.user_popup = folium.Popup(
            iframe, max_width=s.max_height_popup, min_width=s.min_width_popup
        )

        # checks if the profilepicture exist, otherwise render a null.png
        try:
            self.icon = folium.features.CustomIcon(
                icon_image=self.icon_path, icon_size=s.icon_size
            )
        except FileNotFoundError:
            self.icon = folium.features.CustomIcon(
                icon_image="avatars/null.png", icon_size=s.icon_size
            )

    def place_user(self, map):
        """Place out the user to the map"""
        folium.Marker(
            location=self.location,
            popup=self.user_popup,
            tooltip=self.tooltip,
            icon=self.icon,
        ).add_to(map)

    # def fill_map(self, users, map):
    #     """Fills out the map with all users"""
    #     for user in users:
    #         self.place_user(map)

    def _convertLocation(self, location):
        """
        The location from the sheet's type is a string |"57.107118, 12.2520907"|
        and the method converts the string to a list with floats for the script to use
        """
        new_loc = []
        #splits the string to a list to work with
        location = location.split(",")
        for item in location:
            new_loc.append(float(item))
        return new_loc
