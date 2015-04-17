#!/usr/bin/env python
"""Main Flask module. Execute this file to start the HTTP server"""
import os

from flask import Flask, jsonify, request
from flask.ext.iniconfig import INIConfig

from dbclient import api as universe
from routing import JumpGraphProvider as jgp
from networkx import shortest_path

app = Flask(__name__)
INIConfig(app)

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')

with app.app_context():
    app.config.from_inifile('server.ini')


@app.route('/routes/regions/shortest/', methods=['GET'])
def shortest_region_route():
    """Return shortest route between two regions"""
    fromID = request.args.get('from', type=int)
    toID = request.args.get('to', type=int)

    res = shortest_path(jgp().region_jump_graph, fromID, toID)
    return jsonify({'route': res})


@app.route('/systems', methods=['GET'])
def list_systems():
    """Return data about all the static (non-wormhole) systems in the
    EVE Online universe

    Examples:

      $ curl http://127.0.0.1:5000/systems
      {
        "systems": [
          {
            "border": true,
            "constellation": false,
            "constellationID": 20000001,
            ...
          },
          {
           "border": true,
            "constellation": false,
            "constellationID": 20000002,
            ...
          }
          ...
        ]
      }

    """
    # TODO: pagination
    systems = universe.list_systems()

    res = []
    for system in systems:
        res.append(system.as_dict())

    return jsonify({'systems': res})

if __name__ == '__main__':
    app.run()
