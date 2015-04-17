""" SDE Database object-relational configuration.

Module contains mapping between SDE database tables and python classes

"""
from copy import deepcopy
from sqlalchemy import Column, Integer, String, Boolean, REAL
from sqlalchemy.ext.declarative import declarative_base


class _DictableBase(object):
    """Pass this class as `cls` argument to declarative base to add method for
    getting dict representation to all child classes

    """

    def as_dict(self):
        """Return a dictionary of the entry's attribute-value pair, obeying
        custom propery names

        """
        d = deepcopy(self.__dict__)
        d.pop('_sa_instance_state')
        return d

_Base = declarative_base(cls=_DictableBase)


class System(_Base):
    __tablename__ = 'mapSolarSystems'

    regionID = Column(Integer)
    constellationID = Column(Integer)
    id = Column(Integer, primary_key=True, name="solarSystemID")
    name = Column(String(length=100), name='solarSystemName')
    x = Column(REAL)
    y = Column(REAL)
    z = Column(REAL)
    xMin = Column(REAL)
    xMax = Column(REAL)
    yMin = Column(REAL)
    yMax = Column(REAL)
    zMin = Column(REAL)
    zMax = Column(REAL)
    luminosity = Column(REAL)
    border = Column(Boolean)
    fringe = Column(Boolean)
    corridor = Column(Boolean)
    hub = Column(Boolean)
    international = Column(Boolean)
    regional = Column(Boolean)
    constellation = Column(Boolean)
    security = Column(REAL)
    factionID = Column(Integer)
    radius = Column(REAL)
    sunTypeID = Column(Integer)
    securityClass = Column(String(length=2))

    def as_dict(self):
        d = deepcopy(self.__dict__)
        d.pop('_sa_instance_state')
        return d


class Region(_Base):
    __tablename__ = 'mapRegions'

    id = Column(Integer, primary_key=True, name="regionID")
    name = Column(String(length=100),  name="regionName")
    x = Column(REAL)
    y = Column(REAL)
    z = Column(REAL)
    xMin = Column(REAL)
    xMax = Column(REAL)
    yMin = Column(REAL)
    yMax = Column(REAL)
    zMin = Column(REAL)
    zMax = Column(REAL)
    factionID = Column(Integer)
    radius = Column(REAL)


class RegionJump(_Base):
    __tablename__ = 'mapRegionJumps'

    fromID = Column(Integer, primary_key=True, name="fromRegionID")
    toID = Column(Integer, primary_key=True, name="toRegionID")


class ConstellationJump(_Base):
    __tablename__ = 'mapConstellationJumps'

    fromID = Column(Integer,
                    primary_key=True,
                    name="fromConstellationID")
    toID = Column(Integer,
                  primary_key=True,
                  name="toConstellationID")
    fromRegionID = Column(Integer,
                          primary_key=True,
                          name="fromRegionID")
    toRegionID = Column(Integer,
                        primary_key=True,
                        name="toRegionID")


class SystemJump(_Base):
    __tablename__ = 'mapSolarSystemJumps'

    fromID = Column(Integer,
                    primary_key=True,
                    name="fromSolarSystemID")
    toID = Column(Integer,
                  primary_key=True,
                  name="toSolarSystemID")
    fromConstellationID = Column(Integer,
                                 primary_key=True,
                                 name="fromConstellationID")
    toConstellationID = Column(Integer,
                               primary_key=True,
                               name="toConstellationID")
    fromRegionID = Column(Integer,
                          primary_key=True,
                          name="fromRegionID")
    toRegionID = Column(Integer,
                        primary_key=True,
                        name="toRegionID")
