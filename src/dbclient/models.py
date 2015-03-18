""" Mapping between database tables and python classes"""
from sqlalchemy import Column, Integer, String, Boolean, REAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class System(Base):
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


class Region(Base):
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


class RegionJump(Base):
    __tablename__ = 'mapRegionJumps'

    fromRegionID = Column(Integer, primary_key=True)
    toRegionID = Column(Integer, primary_key=True)
