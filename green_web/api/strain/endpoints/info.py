import logging

from flask import request
from flask_restplus import Resource
from green_web.api.restplus import api
from green_web.api.business import get_strain_info, get_strain_coordinates, create_som, list_maps
from green_web.api.serializers import base_strain, strain_coordinates, strain_id_model, som_specs_model, map_factory_msg

log = logging.getLogger(__name__)

ns = api.namespace('strain', description='Operations related to cannabis strains')


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        api.abort(404, "Todo {} doesn't exist".format(todo_id))


parser = api.parser()
parser.add_argument('task', type=str, required=True, help='The task details')


@ns.route('/map')
class MapMaker(Resource):
    """Creates Self-Organizing Maps on demand"""

    @api.expect(som_specs_model)
    @api.marshal_with(map_factory_msg)
    def post(self):
        """Trains a SOM model according to the specifications"""
        # return create_som(som_specs_model)
        return create_som(request.json)


@ns.route('/map/list')
class MapEnlister(Resource):
    """Lists trained Self-Organizing Maps"""

    def get(self):
        """Lists SOM trained model instances"""
        return list_maps()


@ns.route('/<string:strain_id>')
@api.doc(responses={404: 'Strain not found'}, params={'strain_id': 'The Strain ID'}, pattern='silver-haze')
class StrainInfo(Resource):
    """Show a single strain item and lets you not delete them"""
    # @api.doc(notes='todo_id should be in {0}'.format(', '.join(TODOS.keys())))

    @api.marshal_with(base_strain)
    def get(self, strain_id):
        """Fetch a given resource"""
        # abort_if_todo_doesnt_exist(strain_id)
        return get_strain_info(strain_id)

    # @api.expect(strain_id_model)
    @api.marshal_with(strain_coordinates)
    def post(self, strain_id):
        """Fetch the strain coordinates on the self organizing map grid"""
        return get_strain_coordinates(strain_id)
