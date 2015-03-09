import unittest
from mock import Mock

MTO = "MEANINGLESS TEST OUTPUT"
MTI = "MEANINGLESS TEST INPUT"

# Mock sqlite3 module
mock_sqlite3 = Mock()
mock_cursor = mock_sqlite3.connect().cursor
mock_execute = mock_cursor().execute

import sys
sys.modules['sqlite3'] = mock_sqlite3

import dbclient


class TestDbclientMethods(unittest.TestCase):
    def test_list_systems(self):
        mock_execute.return_value = MTO
        res = dbclient.list_systems()

        mock_execute.assert_called_with("SELECT * FROM mapSolarSystems")
        self.assertEqual(res, MTO)

    def test_find_system_by_name(self):
        mock_cursor().fetchone.return_value = MTO
        res = dbclient.find_system_by_name(MTI)

        mock_execute.assert_called_with("SELECT * FROM mapSolarSystems " \
                                        "WHERE solarSystemName=?", (MTI,))
        mock_cursor().fetchone.assert_called_with()
        self.assertEqual(res, MTO)

if __name__ == '__main__':
    unittest.main()
