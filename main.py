from models import RouteSegment, TransitType
from router import TransitGraph

def main():
    network = TransitGraph()

    # Add sample routes across Addis Ababa
    network.add_route(RouteSegment("Bole", "Piazza", 8.5, 15.0, TransitType.ANBESSA_BUS))
    network.add_route(RouteSegment("Bole", "Piazza", 8.5, 25.0, TransitType.MINIBUS))
    network.add_route(RouteSegment("Bole", "Megenagna", 4.0, 10.0, TransitType.SHEGER_BUS))

    print("--- EthioRoute Search: Bole -> Piazza ---")
    direct_routes = network.find_direct_routes("Bole", "Piazza")
    
    for route in direct_routes:
        print(route)

if __name__ == "__main__":
    main()