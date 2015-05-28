"""Public methods for the database client."""
from .models import System, Region, RegionJump, ConstellationJump, SystemJump


def find_system_by_id(id):
    """Find system with specified ID.

    Args:
      id (int): ID of the systen. Negative values will raise
        NegativeIntegerArgumentError

    Returns:
      eve_travel_helper.dbclient.models.System: object representing
        found system
      None: if no system has been found

    """
    query = System.query.filter(System.id == id)
    return query.first()


def find_system_by_name(name):
    """Find solar system with matching name

    Matching is not case-sensitive

    Args:
      name (str): Full name of the system to find

    Returns:
      eve_travel_helper.dbclient.models.System: object representing found
        system
      None: if no system  has been found

    """
    query = System.query.filter(System.name == name)
    return query.first()


def search_systems_by_name(name, page=1, per_page=20):
    """Find solar systems with partially or fully matching names

    Matching is not case-sensitive. Results are paginated.

    Args:
      name (str): Beginning of or full name of the solar system
      page (int, optional): Number of the page to return. Defaults to 1.
      per_page (int, optional): Maximum amount of systems a page will contain.
        Defaults to 20.

    Returns:
      flask_sqlalchemy.Pagination: object containing pagination data

    """
    expr = name + '%'
    query = System.query.order_by(System.name).filter(System.name.like(expr))
    paged = query.paginate(page, per_page, error_out=False)
    return paged


def find_region_by_name(name):
    """Find region with specified name.

    Matching is not case-sensitive

    Args:
      name (str): name of the region

    Returns:
      eve_travel_helper.dbclient.models.Region: object representing
        found region

    """
    query = Region
    query = query.filter(Region.name == name)
    return query.one()


def list_region_jumps():
    """Find all inter-region jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.RegionJump: objects
      representing found regions

    """
    query = RegionJump
    return query.all()


def list_constellation_jumps():
    """Find all inter-constellation jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.RegionJump: objects
        representing found jumps

    """
    query = ConstellationJump
    return query.all()


def list_system_jumps():
    """Find all inter-system jump connections(one for either direction).

    Returns:
      list of eve_travel_helper.dbclient.models.SystemJump: objects
        representing found jump connections

    """
    query = SystemJump
    return query.all()


def list_systems(page=1, per_page=20):
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

    """
    query = System.query.order_by(System.id)
    paged = query.paginate(page, per_page, error_out=False)
    return paged


def count_systems():
    """Count solar systems.

    Returns:
      int: total number of solar systems

    """
    query = System
    return query.count()
