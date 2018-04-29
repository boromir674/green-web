import os
from green_magic import WeedMaster


basedir = os.path.abspath(os.path.dirname(__file__))

data_dir = basedir + '/../../../data'
VARS = ['type', 'effects', 'medical', 'negatives', 'flavors']
DATASET_ID = 'new-dt'
WM = WeedMaster(datasets_dir=data_dir, graphs_dir=data_dir + '/figures')

# WM.create_weedataset(os.path.join(basedir, '../../../../../strain_jsons_2194_fixed_mixed_frow_info.jl'), DATASET_ID)
WM.load_dataset(DATASET_ID + '-clean.pk')
#
# WM.dt.use_variables(VARS)
# WM.dt.clean()
# vectors = WM.get_feature_vectors(WM.dt)
# WM.get_feature_vectors(WM.dt)
# dt = wm.load_dataset('./' + wd + '-clean.pk')

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