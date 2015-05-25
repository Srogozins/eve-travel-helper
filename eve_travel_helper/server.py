#!/usr/bin/env python
"""Main Flask module. Execute this file to start the HTTP server"""
import os

from flask import Flask
from flask.ext.iniconfig import INIConfig
from flask.ext.cors import CORS
from flask_restful import Api

from resources import Systems, Routes

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
INIConfig(app)
cors = CORS(app)

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')

with app.app_context():
    app.config.from_inifile('server.ini')

api.add_resource(Systems,
                 '/systems',
                 '/systems/page/<int:page>',
                 '/systems/<int:id>',
                 '/systems/<string:name>')

api.add_resource(Routes,
                 '/routes/<string:node_type>/<string:route_type>')

if __name__ == '__main__':
    app.run()
