"""Flask resource classes"""
from flask_restful import Resource
from flask import jsonify, request, current_app

from dbclient import api as universe


class Systems(Resource):
    def get(self, page=1):
        """Return paged data about systems in the
        EVE Online universe

        Examples:

          $ curl http://127.0.0.1:5000/systems
          {
            total_systems: 8030,
            systems: [
              {
                border: true,
                constellation: false,
                constellationID: 20000001,
                ...
              },
              {
                border: true,
                constellation: false,
                constellationID: 20000002,
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
        if per_page is None or per_page <= 0:
            per_page = current_app.config['PER_PAGE']

        res = {'systems': [], 'total_systems': 0}

        start = (page - 1) * per_page
        stop = start + per_page
        systems = universe.list_systems(start=start, stop=stop)
        for system in systems:
            res['systems'].append(system.as_dict())

        res['total_systems'] = universe.count_systems()

        return jsonify(res)
