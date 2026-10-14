from models import RouteSegment, TransitType

class TransitGraph:
    def __init__(self):
        self.graph = {}

    def add_station(self, station_name: str):
        if station_name not in self.graph:
            self.graph[station_name] = []