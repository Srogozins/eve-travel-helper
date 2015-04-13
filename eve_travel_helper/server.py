#!/usr/bin/env python
import os

from flask import Flask, jsonify, request
from flask.ext.iniconfig import INIConfig

from routing import JumpGraphProvider as jgp
from networkx import shortest_path

app = Flask(__name__)
INIConfig(app)

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')

with app.app_context():
    app.config.from_inifile('server.ini')


@app.route('/routes/regions/shortest/', methods=['GET'])
def shortest_region_route():
    fromID = request.args.get('from', type=int)
    toID = request.args.get('to', type=int)

    res = shortest_path(jgp().region_jump_graph, fromID, toID)
    return jsonify({'route': res})

if __name__ == '__main__':
    app.run()
