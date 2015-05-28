"""Main Flask module"""
from flask import Flask
from flask_restful import Api

from dbclient.models import db
from resources import Systems, SingleSystem, Routes

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
db.init_app(app)

api.add_resource(Systems,
                 '/systems')
api.add_resource(SingleSystem,
                 '/systems/<int:id>',
                 '/systems/<string:name>')
api.add_resource(Routes,
                 '/routes/<string:node_type>/<string:route_type>')
