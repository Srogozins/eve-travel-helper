import sqlite3

SDE_DIR = "../SDE"
UNIVERSE_DB = SDE_DIR + '/' + "universeDataDx.db"

SQL_LIST_SYSTEMS = 'SELECT * FROM mapSolarSystems'
SQL_FIND_SYSTEM_BY_NAME = 'SELECT * FROM mapSolarSystems ' \
                          'WHERE solarSystemName=?'
SQL_FIND_REGION_BY_NAME = 'SELECT * FROM mapRegions WHERE regionName=?'
SQL_LIST_REGION_JUMPS = 'SELECT * FROM mapRegionJumps'
SQL_GET_JUMPS_FROM_REGION = 'SELECT * FROM mapRegionJumps WHERE fromRegionID=?'

conn = sqlite3.connect(UNIVERSE_DB)
c = conn.cursor()


def list_systems():
    """ Return list of solar systems in universe
    """
    systems = c.execute(SQL_LIST_SYSTEMS)
    return systems


def find_system_by_name(name):
    """ Returns a system with matching name
    """
    c.execute(SQL_FIND_SYSTEM_BY_NAME, (name,))
    return c.fetchone()


def find_region_by_name(name):
    """ Returns a region with matching name
    """
    c.execute(SQL_FIND_REGION_BY_NAME, (name,))
    return c.fetchone()


def list_region_jumps():
    """ Return list of all jumps between regions (in both directions)
    """
    jumps = c.execute(SQL_LIST_REGION_JUMPS)
    return jumps
