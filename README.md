# EthioRoute - Public Transit Optimizer for Addis Ababa

An algorithmic routing engine and multi-modal transit planner designed to calculate optimal travel paths, multi-hop transfers, and accurate fare estimations across Anbessa Bus, Sheger Bus, Light Rail Transit (LRT), and Minibus Taxis in Addis Ababa, Ethiopia.

An algorithmic routing engine for calculating optimal public transit routes (Anbessa Bus, Sheger Bus, LRT, and Minibus Taxis) and fare estimations in Addis Ababa.


- ## Core Features
- **Multi-Modal Data Models**: Strongly typed definitions for transit stations, modes, and network route segments (`models.py`).
- **Dynamic Fare Engine**: Accurate tariff calculation based on transport mode and distance in Ethiopian Birr (ETB) (`fare_calculator.py`).
- **Multi-Hop Route Discovery**: Breadth-First Search (BFS) pathfinding supporting multi-transfer journeys across Addis Ababa (`router.py`).
- **Route Optimization**: Instant filtering by lowest fare cost or shortest physical distance.
- **CLI Interface & Automated Tests**: Command-line interactive search tool backed by a comprehensive unit test suite (`test_router.py`).

## Quickstart
