from models import RouteSegment, TransitType

class TransitGraph:
    def __init__(self):
        self.graph = {}

    def add_station(self, station_name: str):
        if station_name not in self.graph:
            self.graph[station_name] = []
    
    def add_route(self, segment: RouteSegment):
        self.add_station(segment.start_station)
        self.add_station(segment.end_station)
        
        # Add connection in graph
        self.graph[segment.start_station].append(segment)    