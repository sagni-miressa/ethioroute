from dataset import load_addis_transit_network

def run_cli():
    network = load_addis_transit_network()
    print("=== Welcome to EthioRoute (Addis Ababa Public Transit Optimizer) ===")
    print("Available Hubs: Bole, Megenagna, Piazza, Mexico, Merkato, Ayat, CMC, Tor Hailoch\n")

    start = input("Enter Departure Station: ").strip()
    destination = input("Enter Destination Station: ").strip()

    cheapest = network.find_cheapest_route(start, destination)
    shortest = network.find_shortest_route(start, destination)

    print("\n--- RESULTS ---")
    if cheapest:
        print(f"💰 Cheapest Route: {cheapest}")
    else:
        print("❌ No route found for that destination pair.")

    if shortest and shortest != cheapest:
        print(f"⚡ Shortest Route: {shortest}")

if __name__ == "__main__":
    run_cli()