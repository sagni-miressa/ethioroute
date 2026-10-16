# EthioRoute - Public Transit Optimizer for Addis Ababa

An algorithmic routing engine and multi-modal transit planner designed to calculate optimal travel paths, multi-hop transfers, and accurate fare estimations across Anbessa Bus, Sheger Bus, Light Rail Transit (LRT), and Minibus Taxis in Addis Ababa, Ethiopia.

An algorithmic routing engine for calculating optimal public transit routes (Anbessa Bus, Sheger Bus, LRT, and Minibus Taxis) and fare estimations in Addis Ababa.

## Features
- **Data Models**: Multi-modal station & route segment structures (`models.py`)
- **Fare Calculator**: Mode-specific tariff rates in ETB (`fare_calculator.py`)
- **Multi-Hop Search**: BFS multi-transfer journey calculation (`router.py`)
- **Optimizations**: Filter by cheapest fare or shortest distance
- **CLI & Tests**: Interactive interface & unit test validation suite

## Quickstart
