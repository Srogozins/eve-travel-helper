""" Connects to the SDE Database and provides interface for creating sessions
to it
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import config

engine = create_engine('sqlite:///' + config.UNIVERSE_DB, echo=config.LOGGING)
Session = sessionmaker(bind=engine)
