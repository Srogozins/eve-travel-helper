""" Tests for the routing module """
import unittest
from mock import Mock, patch

import test_routing_data as test_data

# Mocking out imported module
mock_dbclient = Mock()
import sys
sys.modules['dbclient'] = mock_dbclient

import routing


class TestGraphMethods(unittest.TestCase):

    @patch('dbclient.api.list_region_jumps')
    def test_graph_rj_with_no_rjs(self, mock_list_region_jumps):
        mock_list_region_jumps.return_value = []
        expected_res = {}

        res = routing.graph_region_jumps()
        mock_list_region_jumps.assert_called_with()
        self.assertEqual(res, expected_res)

    @patch('dbclient.api.list_region_jumps')
    def test_graph_rj_with_2_connected_rjs(self, mock_list_region_jumps):
        mock_list_region_jumps.return_value = test_data.TWO_RJS
        expected_res = {1: [2], 2: [1]}

        res = routing.graph_region_jumps()
        mock_list_region_jumps.assert_called_with()
        self.assertEqual(res, expected_res)

    @patch('dbclient.api.list_region_jumps')
    def test_graph_rj_with_real_rjs(self, mock_list_region_jumps):
        mock_list_region_jumps.return_value = test_data.REAL_RJS

        res = routing.graph_region_jumps()
        mock_list_region_jumps.assert_called_with()
        for rj in test_data.REAL_RJS:
            self.assertIn(rj.fromID, res)
            self.assertIn(rj.toID, res[rj.fromID])


class TestRoutingMethods(unittest.TestCase):

    def test_shortest_routes_with_same_system(self):
        res = routing.shortest_routes('SYSTEM', 'SYSTEM')
        self.assertEqual(res, ['SYSTEM', 'SYSTEM'])

    def test_shortest_region_routes_with_same_region(self):
        res = routing.shortest_routes('REGION', 'REGION')
        self.assertEqual(res, ['REGION', 'REGION'])

if __name__ == '__main__':
    unittest.main()
