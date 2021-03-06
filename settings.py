class Settings:
    def __init__(self):
        """Initialize all the settings for the script"""
        # --Map types -- Changes the looks of the map
        # "cartodbdark_matter"
        # "cartodbpositron"
        # "cartodbpositronnolabels"
        # "cartodbpositrononlylabels"
        # "openstreetmap"
        # "stamenterrain"
        # "stamentoner"
        # "stamentonerbackground"
        # "stamentonerlabels"
        # "stamenwatercolor"
        self.maptype = "stamenwatercolor"

        # -- Places -- Changes the center of the start image
        # Falun     | [60.60357, 15.62597]
        # Varberg   | [57.107118, 12.2520907]
        self.map_location = [60.60357, 15.62597]

        # --Zoom Start-- #Changes the zoom amount, the lower = zoomed out higher = zoomed in
        self.zoom_start = 4

        # ----Scraping----
        # change the link below to the google spreadsheet you want to work from (self.gsheet_url), Makes sure it's public
        self.gsheet_url = "https://docs.google.com/spreadsheets/d/1z1OkOX5dEquICvukzRMA_23aX4gBMV9vDkljinrdMow/edit#gid=0"
        self.use_url = self.gsheet_url.replace("/edit#gid=", "/export?format=csv&gid=")

        # ---Icons----
        size = 50
        self.icon_size = (size, size)

        # ---Popup text----
        self.max_height_popup = 200
        self.min_width_popup = 180
