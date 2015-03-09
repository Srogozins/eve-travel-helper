import sqlite3

SDE_DIR="SDE"
UNIVERSE_DB = SDE_DIR + '/' + "universeDataDx.db"

SQL_LIST_SYSTEMS = 'SELECT * FROM mapSolarSystems'
SQL_FIND_SYSTEM_BY_NAME = 'SELECT * FROM mapSolarSystems WHERE solarSystemName=?'

conn= sqlite3.connect(UNIVERSE_DB);
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
