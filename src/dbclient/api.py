""" Public methods for the database client"""
from .db import Session
from .models import System, Region

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
