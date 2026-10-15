# EthioRoute - Public Transit Optimizer for Addis Ababa

An algorithmic routing engine for calculating optimal public transit routes (Anbessa Bus, Sheger Bus, LRT, and Minibus Taxis) and fare estimations in Addis Ababa.

## Features
- **Data Models**: Multi-modal station & route segment structures (`models.py`)
- **Fare Calculator**: Mode-specific tariff rates in ETB (`fare_calculator.py`)
- **Multi-Hop Search**: BFS multi-transfer journey calculation (`router.py`)
- **Optimizations**: Filter by cheapest fare or shortest distance
- **CLI & Tests**: Interactive interface & unit test validation suite

## Quickstart