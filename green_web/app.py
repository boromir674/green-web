import logging.config
from flask import Flask, Blueprint
from flask_pymongo import PyMongo

from .config import env2config
from .api.restplus import api
from .api.data.endpoints.info import ns as data_info_ns
from .api.strain.endpoints.info import ns as strain_info_ns
# from .api.business import mongo as db


def configure_app(flask_app, environment='development'):
    """
    Configures the input app, based on deployment environment, by setting key-value pairs serving as settings.
    :param flask_app: the app
    :param environment:
    :type environment: one of {'default', 'development', 'testing', 'production'}
    """
    # TODO use config file with inheritance according to environment
    flask_app.config.from_object('green_web.config.' + env2config[environment])
    print('config.' + env2config[environment])
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(strain_info_ns)
    api.add_namespace(data_info_ns)
    flask_app.register_blueprint(blueprint)


def init_app():
    appl = Flask(__name__)
    # db.init_app(appl)
    return appl


app = init_app()
p = '/data/projects/knowfly/green-machine/green-web/logging.conf'
logging.config.fileConfig(p)
logger = logging.getLogger(__name__)
initialize_app(app)

