import logging.config

from flask import Flask, Blueprint

from green_web.config import env2config
from green_web.api.restplus import api
from green_web.api.data.endpoints.info import ns as data_info_ns
from green_web.api.strain.endpoints.info import ns as strain_info_ns

# from green_web.api.data.endpoints.info import ns as data_info_ns

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app, environment='default'):
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


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=app.config['DEBUG'])


if __name__ == "__main__":
    main()
