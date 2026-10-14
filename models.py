class Station:
    def __init__(self, station_id: int, name: str, subcity: str):
        self.station_id = station_id
        self.name = name
        self.subcity = subcity

    def __repr__(self):
        return f"<Station {self.name} ({self.subcity})>"