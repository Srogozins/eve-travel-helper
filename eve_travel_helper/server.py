#!/usr/bin/env python
"""Main Flask module. Execute this file to start the HTTP server"""
import os

from flask import Flask, jsonify, request
from flask.ext.iniconfig import INIConfig
from flask.ext.cors import CORS

from dbclient import api as universe
from routing import JumpGraphProvider as jgp
from networkx import shortest_path

app = Flask(__name__)
INIConfig(app)
cors = CORS(app)

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


@app.route('/systems/', defaults={'page': 1}, methods=['GET'])
@app.route('/systems/page/<int:page>', methods=['GET'])
def list_systems(page):
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

      Pagination examples:

      Both yield first 20 systems
      $ curl http://127.0.0.1:5000/systems
      $ curl http://127.0.0.1:5000/systems/page/1

      Yields second 20 systems
      $ curl http://127.0.0.1:5000/systems/page/2

      Both yield first 10 systems
      $ curl http://127.0.0.1:5000/systems?per_page=10
      $ curl http://127.0.0.1:5000/systems/page/1?per_page=10
    """
    per_page = request.args.get('per_page', type=int)

    if not per_page:
        per_page = app.config['PER_PAGE']

    start = (page - 1) * per_page
    stop = start + per_page

    systems = universe.list_systems(start=start, stop=stop)

    res = []
    for system in systems:
        res.append(system.as_dict())

    return jsonify({'systems': res})

if __name__ == '__main__':
    app.run()
