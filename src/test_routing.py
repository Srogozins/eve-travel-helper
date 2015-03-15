import unittest
from mock import Mock

# Mock dbclient module
mock_dbclient = Mock()

import sys
sys.modules['dbclient'] = mock_dbclient

import routing


class TestRoutingtMethods(unittest.TestCase):
    def test_graph_region_jump(self):
        res = routing.graph_region_jumps()

    def test_shortest_routes_with_same_system(self):
        res = routing.shortest_routes('SYSTEM', 'SYSTEM');
        self.assertEqual(res, ['SYSTEM', 'SYSTEM'])

    def test_shortest_region_routes_with_same_region(self):
        res = routing.shortest_routes('REGION', 'REGION');
        self.assertEqual(res, ['REGION', 'REGION'])

if __name__ == '__main__':
    unittest.main()

