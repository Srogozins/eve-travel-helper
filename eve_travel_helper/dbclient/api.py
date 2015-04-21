"""Public methods for the database client."""
from .session import Session
from .models import System, Region, RegionJump, ConstellationJump, SystemJump

_session = Session()


def find_system_by_name(name):
    """Find solar system with specified name.

    Args:
      name (str): name of the solar system

    Returns:
      eve_travel_helper.dbclient.models.System: object representing
        found system

    Raises:
      sqlalchemy.orm.exc.NoResultFound: If no system with given name was found

    """
    query = _session.query(System)
    query = query.filter(System.name == name)
    return query.one()


def find_region_by_name(name):
    """Find region with specified name.

    Args:
      name (str): name of the region

    Returns:
      eve_travel_helper.dbclient.models.Region: object representing
        found region

    Raises:
      sqlalchemy.orm.exc.NoResultFound: If no region with given name was found

    """
    query = _session.query(Region)
    query = query.filter(Region.name == name)
    return query.one()


def list_region_jumps():
    """Find all inter-region jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.RegionJump: objects
      representing found regions

    """
    query = _session.query(RegionJump)
    return query.all()


def list_constellation_jumps():
    """Find all inter-constellation jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.RegionJump: objects
        representing found jumps

    """
    query = _session.query(ConstellationJump)
    return query.all()


def list_system_jumps():
    """Find all inter-system jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.SystemJump: objects
        representing found jump connections

    """
    query = _session.query(SystemJump)
    return query.all()


def list_systems(start=0, stop=None):
    """List solar systems.

    Args:
        start (int, optional): Offset from which the returned list will start.
          Defaults to 0.
        stop (int, optional): How many systems to include after the offset.
          By default all systems after the offset will be included.

    Returns:
      list of eve_travel_helper.dbclient.models.System: objects
        representing systems

    """
    query = _session.query(System).order_by(System.id).slice(start, stop)
    return query.all()
