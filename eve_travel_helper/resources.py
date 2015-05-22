"""Flask resource classes"""
from flask_restful import Resource
from flask import jsonify, request, current_app

from dbclient import api, exceptions


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
