""" eve_travel_helper.dbclient.session -- main
Connects to the SDE Database and provides interface for creating sessions
to it
"""
import os
from ConfigParser import SafeConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config_file = os.path.join(os.path.dirname(__file__), 'dbclient.ini')
config = SafeConfigParser()
config.read(config_file)

UNIVERSE_DB = config.get('Filepaths', 'UNIVERSE_DB')
LOG = config.getboolean('Logging', 'LOG')

engine = create_engine('sqlite:///' + UNIVERSE_DB, echo=LOG)
Session = sessionmaker(bind=engine)
