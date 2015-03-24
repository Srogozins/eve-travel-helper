""" Tests for the routing module """
import unittest
from mock import Mock, patch, call

import test_routing_data as test_data

# Mocking out imported module
mock_dbclient = Mock()
mock_nx = Mock()
import sys
sys.modules['dbclient'] = mock_dbclient
sys.modules['networkx'] = mock_nx

from routing import JumpGraphProvider, Singleton


class TestJumpGraphProvider(unittest.TestCase):

    @patch('dbclient.api.list_region_jumps')
    @patch('networkx.Graph')
    def _test_graph_region_jumps(self, td_rjs, mock_Graph, mock_list_rjs):
        mock_graph_obj = Mock()
        mock_graph_obj.add_edge = Mock()
        mock_Graph.return_value = mock_graph_obj
        mock_list_rjs.return_value = td_rjs

        res = JumpGraphProvider()._graph_region_jumps()

        self.assertIs(res, mock_graph_obj)

        calls = []
        for rj in td_rjs:
            calls.append(call(rj.fromID, rj.toID))
        mock_graph_obj.add_edge.assert_has_calls(calls)

    def test_graph_region_jumps_zero(self):
        self._test_graph_region_jumps([])

    def test_graph_region_jumps_two(self):
        self._test_graph_region_jumps(test_data.TWO_RJS)

    def test_graph_region_jumps_real(self):
        self._test_graph_region_jumps(test_data.REAL_RJS)

    def tearDown(self):
        # Prevent singleton behaviour for testing
        Singleton._instances.clear()


if __name__ == '__main__':
    unittest.main()
