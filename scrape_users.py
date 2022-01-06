import pandas as pd
from settings import Settings
from convert_to_dictionary import ConvertToDictionary as ctd

s = Settings()


class ScrapeUsers:
    def __init__(self):
        """grabs the data from a gsheet and converts it to a dictionary"""
        self.url = s.use_url
        self.users = pd.read_csv(self.url)
        self.users_dict = ctd(
            self.url
        ).convert()  # omformaterar dataframen till en dictionary

    def display_users(self):
        """displays the users in dictionary form in the terminal"""
        for user in self.users_dict:
            print(user)
