from models import RouteSegment, TransitType
from router import TransitGraph

def load_addis_transit_network() -> TransitGraph:
    graph = TransitGraph()

    routes = [
        # Minibus lines
        RouteSegment("Bole", "Megenagna", 4.5, 12.0, TransitType.MINIBUS),
        RouteSegment("Megenagna", "Piazza", 6.0, 15.0, TransitType.MINIBUS),
        RouteSegment("Bole", "Mexico", 5.0, 14.0, TransitType.MINIBUS),
        RouteSegment("Mexico", "Merkato", 3.5, 10.0, TransitType.MINIBUS),
        RouteSegment("Merkato", "Piazza", 2.0, 7.0, TransitType.MINIBUS),
        
        # Anbessa Bus lines
        RouteSegment("Bole", "Piazza", 9.0, 7.0, TransitType.ANBESSA_BUS),
        RouteSegment("Tor Hailoch", "Mexico", 4.0, 5.0, TransitType.ANBESSA_BUS),
        RouteSegment("Mexico", "Stadium", 2.0, 5.0, TransitType.ANBESSA_BUS),
        
        # Sheger & Light Rail (LRT) Express routes
        RouteSegment("Ayat", "Megenagna", 8.0, 10.0, TransitType.LRT),
        RouteSegment("Megenagna", "Tor Hailoch", 11.0, 12.0, TransitType.LRT),
        RouteSegment("CMC", "Megenagna", 5.5, 8.0, TransitType.SHEGER_BUS),
    ]

    for route in routes:
        graph.add_route(route)

    return graph
