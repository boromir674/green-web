from flask_restplus import fields
from green_web.api.restplus import api

base_strain = api.model('A cannabis strain information', {
    '_id': fields.String(readOnly=True, description='The unique identifier of a strain'),
    'name': fields.String(description='Name of the cannabis strain'),
    'type': fields.String(description='Type of the cannabis strain'),
    'flavors': fields.List(fields.String, description='The mixture of flavors the strain contains')
})

dataset_info = api.model('A Weedataset information', {
    'size': fields.Integer(readOnly=True, description='The number of datapoints'),
    'active_vars': fields.List(fields.String, readOnly=True, description='The set of variables'),
    'vec_len': fields.Integer(readOnly=True, description='The encoded vectors length'),
})

dataset_specs = api.model('A Weedataset specs model', {
    '_id': fields.String(readOnly=True, description='The unique identifier of a strain dataset'),
    'active_vars': fields.List(fields.String, readOnly=True, description='The set of variables', default=['type', 'effects', 'medical', 'negatives', 'flavors'])
})

# dataset_variables = api.model('A set of strain variables', {
#     'set': fields.List(fields., readOnly=True, description='The set of variables')
# })

# pagination = api.model('A page of results', {
#     'page': fields.Integer(description='Number of this page of results'),
#     'pages': fields.Integer(description='Total number of pages of results'),
#     'per_page': fields.Integer(description='Number of items per page of results'),
#     'total': fields.Integer(description='Total number of results'),
# })
#
# page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
#     'items': fields.List(fields.Nested(blog_post))
# })

map_factory_msg = api.model('Map creation outcome information.', {
    'map_id': fields.String(description='The ID given to the som instance created'),
})

som_specs_model = api.model('A Self Organizing Map specifications', {
    'type': fields.String(description='The map\' graph type', default='toroid', pattern='toroid|planar'),
    'grid': fields.String(description='The map\' grid type', default='rectangular', pattern='rectangular|hexagonal'),
    'rows': fields.Integer(description='The number of rows in the map\'s latice', default=20),
    'columns': fields.Integer(description='The number of columns in the map\'s latice', default=20),
    'initialization': fields.String(description='The initialization method of the weight vectors aka codebook', default='pca', pattern='pca|random'),
    # 'specs': fields.String(description='The map factory specifications', default='toroid.15.15.pca')
})

strain_coordinates = api.model('A strain\'s coordinates on a self organizing map grid', {
    'map_specs': fields.Nested(som_specs_model),
    'x': fields.Integer(readOnly=True, description='The x coordinate'),
    'y': fields.Integer(readOnly=True, description='The y coordinate'),
})

strain_id_model = api.model('A cannabis strain ID', {
    'id': fields.String(readOnly=True, description='The unique identifier of a strain', default='silver-haze'),
})
