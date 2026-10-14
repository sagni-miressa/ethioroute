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
    def find_direct_routes(self, start: str, destination: str):
        if start not in self.graph:
            return []
        
        direct_matches = []
        for segment in self.graph[start]:
            if segment.end_station.lower() == destination.lower():
                direct_matches.append(segment)
                
        return direct_matches    