from branca.element import IFrame
import folium


class Map_user:
    """A class tha maps out the user on the map with its info and settings"""

    def __init__(self, user_values):
        '''Contains all the user values in a dictionary type'''
        self.user_values = user_values  # This is a dictionary
        self.icon = f"{self.user_values['name']}.png"
        self.icon_path = f"avatars/{self.icon}"
        #options for the popup bubble
        popup_text = f"Age: {user_values['age']}<br>Sex: {user_values['sex']}"
        iframe = folium.IFrame(popup_text) 
        self.user_popup = folium.Popup(iframe, max_width=200, min_width=180)

        #checks if the profilepicture exist, otherwise render a null.png 
        try:
            self.icon = folium.features.CustomIcon(icon_image=self.icon_path,
                                                   icon_size=(50, 50))
        except FileNotFoundError:
            self.icon = folium.features.CustomIcon(icon_image="avatars/null.png",
                                                   icon_size=(50, 50))

    def splash_user(self, map):
        '''Place out the user to the map'''
        user = self.user_values
        folium.Marker(location=self._convertLocation(user["location"]),
                      popup=self.user_popup,
                      tooltip=user["name"],
                      icon=self.icon).add_to(map)

    def fill_map(self, users, map):
        '''Fills out the map with all users'''
        for user in users:
            self.splash_user(map)

    def _convertLocation(self, location):
        '''
        The location from the sheet's type is a string |"57.107118, 12.2520907"| 
        and the method converts the string to a list with floats for the script to use
        '''
        new_loc = []
        for item in location.split(","):
            new_loc.append(float(item))
        return new_loc
