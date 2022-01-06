import requests
from csv import DictReader

class ConvertToDictionary:
    """Hämtar omformaterar csv med användare till en relevant dictionary"""
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def convert(self):
        '''Matar ut en komplett formaterad dictionary'''
        
        # Hämtar csv genom en google sheet länk som exporterar sheet dokumentet till en csv 
        dataframe = requests.get(self.csv_file, allow_redirects=True) #Sammlar all data från web
        open("users.csv", "wb").write(dataframe.content) #Skapar en fil och fyller med content från r

        #Skapar en dictionary vi kan jobba med från csv filen
        with open("users.csv", "r") as read_obj:
            dict_reader = DictReader(read_obj)

            #packar upp dictionaryn
            list_of_dict = list(dict_reader)
        return list_of_dict
