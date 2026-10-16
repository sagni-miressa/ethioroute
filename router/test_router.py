import unittest
from models import RouteSegment, TransitType
from router import TransitGraph

class TestEthioRoute(unittest.TestCase):
    def setUp(self):
        self.graph = TransitGraph()
        self.graph.add_route(RouteSegment("A", "B", 5.0, 10.0, TransitType.MINIBUS))
        self.graph.add_route(RouteSegment("B", "C", 5.0, 10.0, TransitType.MINIBUS))
        self.graph.add_route(RouteSegment("A", "C", 12.0, 8.0, TransitType.ANBESSA_BUS))

    def test_direct_route(self):
        routes = self.graph.find_direct_routes("A", "C")
        self.assertEqual(len(routes), 1)

    def test_cheapest_route(self):
        cheapest = self.graph.find_cheapest_route("A", "C")
        self.assertIsNotNone(cheapest)
        self.assertEqual(cheapest.total_fare, 8.0)

    def test_shortest_route(self):
        shortest = self.graph.find_shortest_route("A", "C")
        self.assertIsNotNone(shortest)
        self.assertEqual(shortest.total_distance, 10.0)

if __name__ == "__main__":
    unittest.main()