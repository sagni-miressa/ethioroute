from models import TransitType

class FareCalculator:
    BASE_RATES = {
        TransitType.ANBESSA_BUS: 5.0,
        TransitType.SHEGER_BUS: 7.0,
        TransitType.LRT: 6.0,
        TransitType.MINIBUS: 10.0
    }

    @classmethod
    def calculate_fare(cls, mode: TransitType, distance_km: float) -> float:
        base = cls.BASE_RATES.get(mode, 10.0)
        rate_per_km = 1.5 if mode == TransitType.MINIBUS else 0.8
        return round(base + (distance_km * rate_per_km), 2)