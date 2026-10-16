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

class TransitPath:
    def __init__(self, segments: list[RouteSegment]):
        self.segments = segments

    @property
    def total_distance(self) -> float:
        return sum(s.distance_km for s in self.segments)

    @property
    def total_fare(self) -> float:
        return sum(s.fare_etb for s in self.segments)

    @property
    def transfers(self) -> int:
        return max(0, len(self.segments) - 1)

    def __repr__(self):
        if not self.segments:
            return "<Path: Empty>"
        stops = " -> ".join([self.segments[0].start_station] + [s.end_station for s in self.segments])
        return f"<Path: {stops} | Total: {self.total_distance:.1f}km, {self.total_fare:.2f} ETB, {self.transfers} transfers>"