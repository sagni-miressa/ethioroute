from enum import Enum

class TransitType(Enum):
    MINIBUS = "Minibus Taxi"
    ANBESSA_BUS = "Anbessa Bus"
    SHEGER_BUS = "Sheger Bus"
    LRT = "Light Rail Transit"

class Station:
    def __init__(self, station_id: int, name: str, subcity: str):
        self.station_id = station_id
        self.name = name
        self.subcity = subcity

    def __repr__(self):
        return f"<Station {self.name} ({self.subcity})>"

class RouteSegment:
    def __init__(self, start_station: str, end_station: str, distance_km: float, fare_etb: float, mode: TransitType):
        self.start_station = start_station
        self.end_station = end_station
        self.distance_km = distance_km
        self.fare_etb = fare_etb
        self.mode = mode

    def __repr__(self):
        return f"<{self.mode.value}: {self.start_station} -> {self.end_station} ({self.distance_km}km, {self.fare_etb} ETB)>"