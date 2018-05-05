import os
from flask_pymongo import PyMongo
from green_magic import WeedMaster


mongo = PyMongo()
basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, '../../data')
strains_jl = os.path.join(data_dir, 'strain_jsons_2194_fixed_mixed_frow_info.jl')

print(basedir)
print(data_dir)
print(strains_jl)

VARS = ['type', 'effects', 'medical', 'negatives', 'flavors']
DATASET_ID = 'new-dt'

WM = WeedMaster(datasets_dir=data_dir, graphs_dir=data_dir + '/figures')
WM.load_dataset(DATASET_ID + '-clean.pk')

# /data/projects/knowfly/green-machine/green-web/green_web/api/../../data/strain_jsons_2194_fixed_mixed_frow_info.jl

# WM.create_weedataset(strains_jl, DATASET_ID)


# WM.dt.use_variables(VARS)
# WM.dt.clean()
# vectors = WM.get_feature_vectors(WM.dt)
# _ = WM.get_feature_vectors(WM.dt)

# cls = WM.cluster_manager.get_clusters(som, nb_clusters=10)
# cls.print_clusters(threshold=7, prec=3)

# WM.save_dataset(DATASET_ID)


def get_strain_info(strain_id):
    return WM.dt[strain_id]


def get_strain_coordinates(strain_id):
    print(type(WM.dt))
    # print(WM.dt.id2index)
    x = WM.som.bmus[WM.dt.id2index[strain_id]][0]

    y = WM.som.bmus[WM.dt.id2index[strain_id]][1]
    print(WM.map_manager.map_obj2id)
    print(WM.som)
    print(WM.som in WM.map_manager.map_obj2id)
    return {
        'map_specs': mapid2specs(WM.map_manager.map_obj2id[WM.som]),
        'x': x,
        'y': y
    }


def create_som(som_specs_model):
    specs_string = '.'.join(map(lambda x: str(x), (som_specs_model['type'], som_specs_model['grid'], som_specs_model['rows'], som_specs_model['columns'], som_specs_model['initialization'])))
    som = WM.map_manager.get_som(specs_string)
    print(som == WM.som)
    print(som in WM.map_manager.map_obj2id)
    print(WM.som in WM.map_manager.map_obj2id)
    return {
        'map_id': WM.map_manager.map_obj2id[som]
    }


def list_maps():
    return {'maps': sorted([map_id for map_id in WM.map_manager.id2map_obj.keys()])}


def mapid2specs(mapid):
    return {'type': mapid.split('_')[3],
            'grid': mapid.split('_')[4],
            'rows': mapid.split('_')[5],
            'columns': mapid.split('_')[6],
            'initialization': mapid.split('_')[2]}


def create_dataset(dataset_specs):
    # print(strains_jl)
    # print('/data/projects/knowfly/green-machine/green-web/green_web/api/../../data/strain_jsons_2194_fixed_mixed_frow_info.jl')
    dt = WM.create_weedataset(strains_jl, dataset_specs['_id'])
    dt.use_variables(dataset_specs['active_vars'])
    dt.clean()
    _ = WM.get_feature_vectors(dt)
    WM.save_dataset(dataset_specs['_id'])
    return {
        'size': len(dt),
        'active_vars': dt.active_variables,
        'vec_len': len(dt.datapoints[0])
    }


def load_dataset(dataset_id):
    WM.load_dataset(dataset_id + '-clean.pk')
    return {
        'size': len(WM.dt),
        'active_vars': WM.dt.active_variables,
        'vec_len': len(WM.dt.datapoints[0])
    }
