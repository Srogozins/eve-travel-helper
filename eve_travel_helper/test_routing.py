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

    @patch('dbclient.api.list_constellation_jumps')
    @patch('networkx.Graph')
    def _test_graph_constellation_jumps(self,
                                        td_cjs,
                                        mock_Graph,
                                        mock_list_cjs):
        mock_graph_obj = Mock()
        mock_graph_obj.add_edge = Mock()
        mock_Graph.return_value = mock_graph_obj
        mock_list_cjs.return_value = td_cjs

        res = JumpGraphProvider()._graph_constellation_jumps()

        self.assertIs(res, mock_graph_obj)

        calls = []
        for cj in td_cjs:
            calls.append(call(cj.fromID, cj.toID))
        mock_graph_obj.add_edge.assert_has_calls(calls)

    @patch('dbclient.api.list_system_jumps')
    @patch('networkx.Graph')
    def _test_graph_system_jumps(self,
                                 td_sjs,
                                 mock_Graph,
                                 mock_list_sjs):
        mock_graph_obj = Mock()
        mock_graph_obj.add_edge = Mock()
        mock_Graph.return_value = mock_graph_obj
        mock_list_sjs.return_value = td_sjs

        res = JumpGraphProvider()._graph_system_jumps()

        self.assertIs(res, mock_graph_obj)

        calls = []
        for sj in td_sjs:
            calls.append(call(sj.fromID, sj.toID))
        mock_graph_obj.add_edge.assert_has_calls(calls)

    def setUp(self):
        # Prevent singleton behaviour for testing
        Singleton._instances.clear()

    def test_graph_region_jumps_zero(self):
        self._test_graph_region_jumps([])

    def test_graph_region_jumps_two(self):
        self._test_graph_region_jumps(test_data.TWO_RJS)

    def test_graph_region_jumps_real(self):
        self._test_graph_region_jumps(test_data.REAL_RJS)

    def test_graph_constellation_jumps_zero(self):
        self._test_graph_constellation_jumps([])

    def test_graph_constellation_jumps_two(self):
        self._test_graph_constellation_jumps(test_data.TWO_RJS)

    def test_graph_constellation_jumps_real(self):
        self._test_graph_constellation_jumps(test_data.REAL_RJS)

    def test_graph_system_jumps_zero(self):
        self._test_graph_system_jumps([])

    def test_graph_system_jumps_two(self):
        self._test_graph_system_jumps(test_data.TWO_RJS)

    def test_graph_system_jumps_real(self):
        self._test_graph_system_jumps(test_data.REAL_RJS)

    def tearDown(self):
        # Prevent singleton behaviour for testing
        Singleton._instances.clear()


if __name__ == '__main__':
    unittest.main()
