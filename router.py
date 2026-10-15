from collections import deque
from models import RouteSegment, TransitType, TransitPath

class TransitGraph:
    def __init__(self):
        self.graph = {}

    def add_station(self, station_name: str):
        if station_name not in self.graph:
            self.graph[station_name] = []

    def add_route(self, segment: RouteSegment):
        self.add_station(segment.start_station)
        self.add_station(segment.end_station)
        self.graph[segment.start_station].append(segment)

    def find_direct_routes(self, start: str, destination: str):
        if start not in self.graph:
            return []
        
        direct_matches = []
        for segment in self.graph[start]:
            if segment.end_station.lower() == destination.lower():
                direct_matches.append(segment)
                
        return direct_matches

    def find_all_paths(self, start: str, destination: str, max_transfers: int = 2) -> list[TransitPath]:
        if start not in self.graph or destination not in self.graph:
            return []

        results = []
        queue = deque([(start, [])])

        while queue:
            current_station, path = queue.popleft()

            if current_station.lower() == destination.lower() and path:
                results.append(TransitPath(path))
                continue

            if len(path) > max_transfers:
                continue

            for segment in self.graph.get(current_station, []):
                visited_stations = [s.start_station for s in path] + [s.end_station for s in path]
                if segment.end_station not in visited_stations:
                    queue.append((segment.end_station, path + [segment]))

        return results