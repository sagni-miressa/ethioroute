from dataset import load_addis_transit_network

def main():
    network = load_addis_transit_network()

    origin = "Bole"
    destination = "Piazza"

    print("==================================================")
    print(f" ETHIOROUTE OPTIMIZER: {origin} -> {destination}")
    print("==================================================")

    paths = network.find_all_paths(origin, destination)
    print(f"\nFound {len(paths)} total connection path(s):")
    for idx, path in enumerate(paths, 1):
        print(f" Option {idx}: {path}")

    cheapest = network.find_cheapest_route(origin, destination)
    shortest = network.find_shortest_route(origin, destination)

    print("\n--- OPTIMAL CHOICES ---")
    print(f"Best Value  : {cheapest}")
    print(f"Most Direct : {shortest}")

if __name__ == "__main__":
    main()