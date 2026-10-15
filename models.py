from enum import Enum
from fare_calculator import FareCalculator

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
    def __init__(self, start_station: str, end_station: str, distance_km: float, fare_etb: float = 0.0, mode: TransitType = TransitType.MINIBUS):
        self.start_station = start_station
        self.end_station = end_station
        self.distance_km = distance_km
        self.mode = mode
        self.fare_etb = fare_etb if fare_etb > 0 else FareCalculator.calculate_fare(mode, distance_km)

    def is_valid(self) -> bool:
        return self.distance_km > 0 and self.fare_etb >= 0

    def __repr__(self):
        return f"<{self.mode.value}: {self.start_station} -> {self.end_station} ({self.distance_km}km, {self.fare_etb} ETB)>"