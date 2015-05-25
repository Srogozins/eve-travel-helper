#!/usr/bin/env python
"""Run this script to start the flask application server"""
import os

from flask.ext.iniconfig import INIConfig
from flask.ext.cors import CORS

from eve_travel_helper.server import app

INIConfig(app)
cors = CORS(app)

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')

with app.app_context():
    app.config.from_inifile('server.ini')

if __name__ == '__main__':
    app.run()
