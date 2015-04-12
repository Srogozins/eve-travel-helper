""" Public methods for the database client"""
from .db import Session
from .models import System, Region, RegionJump, ConstellationJump, SystemJump

session = Session()


def find_system_by_name(name):
    """ Returns System object representing a system in DB with matching name

        If there's more than one system with matching name,
        throws MultipleResultsFound
        If no system with matching name was found, throws NoResultFound
    """

    query = session.query(System)
    query = query.filter(System.name == name)
    return query.one()


def find_region_by_name(name):
    """ Returns Region object representing a region in DB with matching name

        If there's more than one region with matching name,
        throws MultipleResultsFound
        If no region with matching name was found, throws NoResultFound
    """

    query = session.query(Region)
    query = query.filter(Region.name == name)
    return query.one()


def list_region_jumps():
    """ Returns a list of RegionJump objects matching all entries for jump
    connections between regions (an object for each direction)
    """

    query = session.query(RegionJump)
    return query.all()


def list_constellation_jumps():
    """ Returns a list of ConstellationJump objects matching all entries for
    jump connections between constellation (an object for each direction)
    """

    query = session.query(ConstellationJump)
    return query.all()


def list_system_jumps():
    """ Returns a list of SystemJump objects matching all entries for
    jump connections between systems (an object for each direction)
    """

def list_systems():
    """ Returns a list of System objects, matching all entries for systems"""

    query = session.query(System)
    return query.all()
