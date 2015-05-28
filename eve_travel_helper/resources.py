"""Flask resource classes"""
from flask_restful import abort, reqparse, Resource
from flask import jsonify, current_app

from dbclient import api
from routing import shortest_system_route, NodeNotInGraphError

system_arg_parser = reqparse.RequestParser()
system_arg_parser.add_argument('page',
                               default=1,
                               type=int,
                               location='args')
system_arg_parser.add_argument('per_page',
                               type=int,
                               location='args')
system_arg_parser.add_argument('name',
                               type=str,
                               location='args')


class Systems(Resource):
    def get(self):
        """Return data about systems in the EVE Online universe

        """
        args = system_arg_parser.parse_args()
        res = {'systems': [], 'total_systems': 0}
        per_page = args['per_page']
        if per_page is None or per_page <= 0:
            per_page = current_app.config['PER_PAGE']

        if args['name']:
            paged = api.search_systems_by_name(args['name'], args['page'], per_page)
        else:
            paged = api.list_systems(args['page'], per_page)

        res['systems'] = [s.as_dict() for s in paged.items]
        res['total_systems'] = paged.total

        return jsonify(res)


class SingleSystem(Resource):
    def get(self, id=None, name=None):
        """Return data about a specific system in the EVE Online universe

        """
        res = {'systems': [], 'total_systems': 0}

        if id is not None:
            system = api.find_system_by_id(id)
            if system is not None:
                res['systems'].append(system.as_dict())
            res['total_systems'] = len(res['systems'])
        elif name is not None:
            system = api.find_system_by_name(name)
            if system is not None:
                res['systems'].append(system.as_dict())
            res['total_systems'] = len(res['systems'])
        return jsonify(res)


route_arg_parser = reqparse.RequestParser()
route_arg_parser.add_argument('waypoints',
                              type=int,
                              action='append',
                              required=True,
                              location=['json'])


class Routes(Resource):
    """Calculate and return routes

    """
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
                    route = shortest_system_route(w1, w2)
                    route2 = [api.find_system_by_id(s_id).as_dict() for s_id in route]
                    res['route'].append(route2)
            except NodeNotInGraphError as e:
                abort(409, message=e.msg)

        return jsonify(res)
