#!/usr/bin/env python
"""Main Flask module. Execute this file to start the HTTP server"""
import os

from flask import Flask, jsonify, request
from flask.ext.iniconfig import INIConfig
from flask.ext.cors import CORS
from flask_restful import Api


from routing import JumpGraphProvider as jgp
from resources import Systems
from networkx import shortest_path

app = Flask(__name__)
api = Api(app)
INIConfig(app)
cors = CORS(app)

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')

with app.app_context():
    app.config.from_inifile('server.ini')

api.add_resource(Systems,
                 '/systems',
                 '/systems/page/<int:page>')


@app.route('/routes/regions/shortest/', methods=['GET'])
def shortest_region_route():
    """Return shortest route between two regions"""
    fromID = request.args.get('from', type=int)
    toID = request.args.get('to', type=int)

    res = shortest_path(jgp().region_jump_graph, fromID, toID)
    return jsonify({'route': res})


@app.route('/routes/systems/shortest/', methods=['GET'])
def shortest_system_route():
    """Return shortest route between two systems"""
    fromID = request.args.get('from', type=int)
    toID = request.args.get('to', type=int)

    res = shortest_path(jgp().system_jump_graph, fromID, toID)
    return jsonify({'route': res})

if __name__ == '__main__':
    app.run()
