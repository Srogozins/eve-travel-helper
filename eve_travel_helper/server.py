#!/usr/bin/python
from flask import Flask, jsonify, request
from routing import JumpGraphProvider as jgp
from networkx import shortest_path

app = Flask(__name__)


@app.route('/routes/regions/shortest/', methods=['GET'])
def shortest_region_route():
    fromID = request.args.get('from', type=int)
    toID = request.args.get('to', type=int)

    res = shortest_path(jgp().region_jump_graph, fromID, toID)
    return jsonify({'route': res})

if __name__ == '__main__':
    app.run(debug=True)
