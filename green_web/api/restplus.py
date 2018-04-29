import logging
# import traceback

from flask_restplus import Api


log = logging.getLogger(__name__)

api = Api(version='0.1', title='Green Machine API',
          description='A web API for the Green Machine powered by Flask RestPlus')


# @api.errorhandler
# def default_error_handler(_):
#     message = 'An unhandled exception occurred.'
#     log.exception(message)
#
#     if not settings.FLASK_DEBUG:
#         return {'message': message}, 500
#
#
# @api.errorhandler(NoResultFound)
# def database_not_found_error_handler(_):
#     log.warning(traceback.format_exc())
#     return {'message': 'A database result was required but none was found.'}, 404
