"""Flask resource classes"""
from flask_restful import abort, reqparse, Resource
from flask import jsonify, request, current_app

from dbclient import api, exceptions
from routing import shortest_system_route, NodeNotInGraphError


class Systems(Resource):
    def get(self, id=None, name=None, page=1):
        """Return data about systems in the EVE Online universe

        """
        res = {'systems': [], 'total_systems': 0}

        if id is not None:
            try:
                system = api.find_system_by_id(id)
                if system is not None:
                    res['systems'].append(system.as_dict())
            except exceptions.NegativeIntegerError:
                res['systems']
            res['total_systems'] = len(res['systems'])
        elif name is not None:
            system = api.find_system_by_name(name)
            if system is not None:
                res['systems'].append(system.as_dict())
            res['total_systems'] = len(res['systems'])
        else:
            per_page = request.args.get('per_page', type=int)
            if per_page is None or per_page <= 0:
                per_page = current_app.config['PER_PAGE']

            start = (page - 1) * per_page
            stop = start + per_page

            systems = api.list_systems(start=start, stop=stop)
            res['systems'] = [s.as_dict() for s in systems]
            res['total_systems'] = api.count_systems()

        return jsonify(res)

route_arg_parser = reqparse.RequestParser()
route_arg_parser.add_argument('waypoints',
                              type=int,
                              action='append',
                              required=True,
                              location=['json'])


class Routes(Resource):
    def post(self, node_type=None, route_type='shortest'):
        """Calculate routes

        """
        node_types = ['systems', 'constellations', 'regions']
        route_types = ['shortest']
        res = {'route': []}

        if node_type in node_types and route_type in route_types:
            args = route_arg_parser.parse_args()
            waypoints = args['waypoints']
            try:
                # calculate route slices for every pair of neighbor waypoints
                # and the list and append it to the route
                for w1, w2 in zip(waypoints, waypoints[1:]):
                    res['route'].append(shortest_system_route(w1, w2))
            except NodeNotInGraphError as e:
                abort(409, message=e.msg)

        return jsonify(res)
