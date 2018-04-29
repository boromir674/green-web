import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

env2config = {
    'default': 'DevelopmentConfig',
    'production': 'ProductionConfig',
    'development': 'DevelopmentConfig',
    'testing': 'TestingConfig',
}


class BaseConfig(object):
    """Common configurations. Put any configurations here that are common across all environments."""
    DEBUG = False
    TESTING = False
    APPLICATION_ROOT = "/api/"
    APP_NAME = 'STRAIN MAP'
    # URL_PREFIX = '/api/v1.0.0'
    # HOST='0.0.0.0'
    # BOOTSWATCH_THEME = "slate"
    # SQLALCHEMY_ECHO = True # Allow SQLAlchemy to log errors
    # ADMIN_EMAIL = "your_email@gmail.com"
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'  # one of :{'none', 'list', 'full'}
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False  # TODO experiment with True

    # ERROR_404_HELP = True  # True is the default value: if false than if a request does not match any endpoint, the app
    # suggests other endpoints that closely match the requested endpoint.

    # Asset files
    UPLOAD_FOLDER = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    # limit the maximum allowed payload to 16 megabytes.
    # If a larger file is transmitted, Flask will raise an RequestEntityTooLarge exception.
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    THUMBNAIL_SIZE = 128, 128
    MAX_SIZE = 1600
    PERMANENT_SESSION_LIFETIME = 2500000  # TODO: Temporal cheat around the json serialization

    def __init__(self):  # these cannot be used as i.e. app.config['DATA_PATH']
        self.DATA_PATH = os.path.join(basedir, 'data')
        self.OUTPUT_FOLDER = os.path.join(basedir, 'output')
        self.LOCAL_LOG = os.path.join(self.OUTPUT_FOLDER, 'log')
        self.PACKAGE_FOLDERS = []
        # if not hasattr(self, 'FIELD_ALPHA'):
        #     self.FIELD_ALPHA = False


class DevelopmentConfig(BaseConfig):
    """Development configurations"""
    SECRET_CONFIG = 'dev-config.py'
    SERVER_NAME = "localhost:5555"
    # PORT = 5000
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configurations"""
    SECRET_CONFIG = 'test-config.py'
    SERVER_NAME = "localhost:5555"
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configurations"""
    SECRET_CONFIG = 'prod-config.py'
    # APP_URL = "quickandclean.org"
    PORT = 80
    DEBUG = False
    SQLALCHEMY_ECHO = False
