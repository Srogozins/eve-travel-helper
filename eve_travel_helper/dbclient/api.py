"""Public methods for the database client."""
from sqlalchemy.orm.exc import NoResultFound

from .exceptions import NegativeIntegerError
from .session import Session
from .models import System, Region, RegionJump, ConstellationJump, SystemJump

_session = Session()


def catch_noresults(return_list=False):
    """Decorator to prevent sqlalchemy's NoResultFound exception from leaking.

    Said exception will be caught and a value will be returned.

    Args:
        return_list (bool, optional): If true, when NoResultFound is caught,
          an empty list will be returned. Otherwise None will be returned.

        """
    def catch_noresults_decorator(func):
        def catcher(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except NoResultFound:
                if return_list:
                    return []
                else:
                    return None
        return catcher
    return catch_noresults_decorator


@catch_noresults()
def find_system_by_id(id):
    """Find system with specified ID.

    Args:
      id (int): ID of the systen. Negative values will raise
        NegativeIntegerError

    Returns:
      eve_travel_helper.dbclient.models.System: object representing
        found system

    Raises:
      NegativeIntegerError: If a negative integer is passed as a value
        for an argument for which it is illegal

    """
    if id < 0:
        raise NegativeIntegerError(id)

    query = _session.query(System)
    query = query.filter(System.id == id)
    return query.one()


@catch_noresults()
def find_system_by_name(name):
    """Find solar system with matching name

    Matching is not case-sensitive

    Args:
      name (str): Full name of the system to find

    Returns:
      eve_travel_helper.dbclient.models.System: object representing found
        system

    """
    query = _session.query(System)
    query = query.filter(System.name == name)
    return query.one()


@catch_noresults(return_list=False)
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


@catch_noresults()
def find_region_by_name(name):
    """Find region with specified name.

    Matching is not case-sensitive

    Args:
      name (str): name of the region

    Returns:
      eve_travel_helper.dbclient.models.Region: object representing
        found region

    """
    query = _session.query(Region)
    query = query.filter(Region.name == name)
    return query.one()


@catch_noresults(return_list=True)
def list_region_jumps():
    """Find all inter-region jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.RegionJump: objects
      representing found regions

    """
    query = _session.query(RegionJump)
    return query.all()


@catch_noresults(return_list=True)
def list_constellation_jumps():
    """Find all inter-constellation jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.RegionJump: objects
        representing found jumps

    """
    query = _session.query(ConstellationJump)
    return query.all()


@catch_noresults(return_list=True)
def list_system_jumps():
    """Find all inter-system jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.SystemJump: objects
        representing found jump connections

    """
    query = _session.query(SystemJump)
    return query.all()


@catch_noresults(return_list=True)
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
