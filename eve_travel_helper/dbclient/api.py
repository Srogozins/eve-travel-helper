"""Public methods for the database client."""
from .session import Session
from .models import System, Region, RegionJump, ConstellationJump, SystemJump

_session = Session()


class NegativeIntegerError(ValueError):
    """Exception for illegal negative integer values

    Args:
      value (int): The offending value.

    Attributes:
      msg (str): Human readable string describing the exception and
        displaying the offending value

    """
    def __init__(self, value):
        self.msg = 'Illegal value for `start` argument: %i. \
                    Cannot be negative' % value


def find_system_by_id(id):
    """Find system with specified ID.

    Args:
      id (int): ID of the systen. Negative values will raise
        NegativeIntegerError

    Returns:
      eve_travel_helper.dbclient.models.System: object representing
        found system

    Raises:
      sqlalchemy.orm.exc.NoResultFound: If no system with given ID was found
      NegativeIntegerError: If a negative integer is passed as a value
        for an argument for which it is illegal

    """
    if id < 0:
        raise NegativeIntegerError(id)

    query = _session.query(System)
    query = query.filter(System.id == id)
    return query.one()


def find_system_by_name(name):
    """Find solar system with matching name

    Matching is not case-sensitive

    Args:
      name (str): Full name of the system to find

    Returns:
      eve_travel_helper.dbclient.models.System: object representing found
        system

    Raises:
      sqlalchemy.orm.exc.NoResultFound: If no system with matching name was
        found

    """
    query = _session.query(System)
    query = query.filter(System.name == name)
    return query.one()


def search_systems_by_name(name, exact_match=False, start=0, stop=None):
    """Find solar systems with matching names

    Matching is not case-sensitive

    Args:
      name (str): Beginning part or full name of the solar system
      exact_match (bool): Whether to match the name exactly instead of taking
        the name argument as incoplete beginning of the name. Default false.
      start (int, optional): Offset from which the returned list will start.
        Defaults to 0. Negative values will raise ValueError
      stop (int, optional): How many systems to include after the offset.
        By default all systems after the offset will be included.
        Negative values will raise ValueError

    Returns:
      list of eve_travel_helper.dbclient.models.System: objects representing
        matched systems

    Raises:
      sqlalchemy.orm.exc.NoResultFound: If no systems with matching names were
        found
      NegativeIntegerError: If a negative integer is passed as a value
        for an argument for which it is illegal

    """
    if start < 0:
        raise NegativeIntegerError(start)

    if stop is not None and stop < 0:
        raise NegativeIntegerError(stop)

    query = _session.query(System)

    if exact_match:
        return [find_system_by_name(name)]
    else:
        expr = name + '%'
        query = query.filter(System.name.like(expr))
        query = query.order_by(System.id).slice(start, stop)

        return query.all()


def find_region_by_name(name):
    """Find region with specified name.

    Matching is not case-sensitive

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
        Defaults to 0. Negative values will raise ValueError
      stop (int, optional): How many systems to include after the offset.
        By default all systems after the offset will be included.
        Negative values will raise ValueError

    Returns:
      list of eve_travel_helper.dbclient.models.System: objects
        representing systems

    Raises:
      sqlalchemy.orm.exc.NoResultFound: If no systems with matching
        names were found
      NegativeIntegerError: If a negative integer is passed as a value
        for an argument for which it is illegal

    """
    if start < 0:
        raise NegativeIntegerError(start)

    if stop is not None and stop < 0:
        raise NegativeIntegerError(stop)

    query = _session.query(System).order_by(System.id).slice(start, stop)
    return query.all()


def count_systems():
    """Count solar systems.

    Returns:
      int: total number of solar systems

    """
    query = _session.query(System)
    return query.count()
