import pandas as pd
from convert_to_dictionary import ConvertToDictionary as ctd
class Users:
    def __init__(self):
        self.sheet_url = "https://docs.google.com/spreadsheets/d/1z1OkOX5dEquICvukzRMA_23aX4gBMV9vDkljinrdMow/edit#gid=0"
        self.url = self.sheet_url.replace("/edit#gid=","/export?format=csv&gid=")
        self.users = pd.read_csv(self.url)
        self.users_dict = ctd(self.url).convert() # omformaterar dataframen till en dictionary

    def display_users(self):
        for user in self.users_dict:
            print(user)


u = Users()
u.display_users()
print(u.users_dict)
