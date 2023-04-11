import networkx as nx

try: from .to_current_society import ToCurrentSociety
except: from to_current_society import ToCurrentSociety


class CurrentSociety(ToCurrentSociety):

    def __init__(self, society, start_date=None, end_date=None):
        self.society = society
        self.env = self.society.env
        self.G = nx.Graph()
        self.to_current_society(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date
        super().__init__()

    def __str__(self):
        return str(self.G)