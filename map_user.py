import folium

class Map_user:
    """A class tha maps out the user on the map with its info and settings"""
    def __init__(self, location, user_pic="none.png", user_popup="None"):
        self.location = location
        self.user_pic = user_pic
        self.user_popup = f"<i>{user_popup}</i>"
        self.icon = folium.features.CustomIcon(icon_image=user_pic,
                                               icon_size=(50, 50))
