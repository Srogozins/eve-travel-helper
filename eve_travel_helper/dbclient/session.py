"""SDE database session interface.

Connects to the SDE Database using given configuration and provides interface
for creating sessions to it

Attributes:
  Session(sqlalchemy.orm.session.Session): Database session factory object

"""
import os
from ConfigParser import SafeConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_config_file = os.path.join(os.path.dirname(__file__), 'dbclient.ini')
_config = SafeConfigParser()
_config.read(_config_file)

_UNIVERSE_DB = _config.get('Filepaths', 'UNIVERSE_DB')
_LOG = _config.getboolean('Logging', 'LOG')

_engine = create_engine('sqlite:///' + _UNIVERSE_DB, echo=_LOG)
Session = sessionmaker(bind=_engine)
