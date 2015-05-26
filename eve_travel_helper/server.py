"""Main Flask module"""
from flask import Flask
from flask_restful import Api

from resources import Systems, SystemSearch, Routes

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

api.add_resource(Systems,
                 '/systems',
                 '/systems/page/<int:page>',
                 '/systems/<int:id>',
                 '/systems/<string:name>')

api.add_resource(SystemSearch,
                 '/systems/search')

api.add_resource(Routes,
                 '/routes/<string:node_type>/<string:route_type>')
