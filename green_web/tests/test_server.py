import os
import sys
import json
import unittest
import tempfile
import requests
from random import randint

from green_web import green_app

# Random order for tests runs. (Original is: -1 if x<y, 0 if x==y, 1 if x>y).
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: randint(-1, 1)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        # self.db_fd, green_app.config['DATABASE'] = tempfile.mkstemp()
        green_app.testing = True
        self.app = green_app.test_client()
        self.strain_id1 = 'amnesia'
        self.strain_id2 = 'silver-haze'
        self.map_specs1 = {
            'columns': 5,
            'grid': 'hexagonal',
            'initialization': 'pca',
            'rows': 7,
            'type': 'toroid'
        }
        self.map_specs2 = {
            'columns': 4,
            'grid': 'rectangular',
            'initialization': 'random',
            'rows': 8,
            'type': 'planar'
        }
        # TODO decouple the 'new-dt' component of the id
        self.map_id1 = 'somoclu_new-dt_pca_toroid_hexagonal_7_5'
        self.map_id2 = 'somoclu_new-dt_random_planar_rectangular_8_4'
        _ = self.app.post('/api/strain/map', data=json.dumps(self.map_specs1), headers={"Content-Type": "application/json"})
        # data = json.loads(response.get_data(as_text=True))
        # self.map_id2 = "somoclu_new-dt_pca_toroid_rectangular_20_10"
        # with green_app.app_context():
        #     flaskr.init_db()

    def tearDown(self):
        pass
        # os.close(self.db_fd)
        # os.unlink(flaskr.app.config['DATABASE'])

    def test_strain_id_endpoint(self):
        response = self.app.get('/api/strain/'+self.strain_id1)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('flavors', data)
        self.assertIn('name', data)
        self.assertIn('type', data)
        self.assertEqual(data['flavors'], ['Earthy', 'Sweet', 'Pungent'])
        self.assertEqual(data['name'], 'amnesia')
        self.assertEqual(data['type'], 'sativa')

    def test_map_creation_endpoint(self):
        response = self.app.post('/api/strain/map', data=json.dumps(self.map_specs2), headers={"Content-Type": "application/json"})
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('map_id', data)
        self.assertEqual(data['map_id'], self.map_id2)

    def test_strain_coordinates_request(self):
        response = self.app.post('/api/strain/' + self.strain_id2)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(float(data['x']), int(data['x']))
        self.assertEqual(float(data['y']), int(data['y']))
        self.assertGreaterEqual(int(data['x']), 0)
        self.assertGreaterEqual(int(data['y']), 0)
        self.assertLessEqual(int(data['x']), int(data['map_specs']['columns']))
        self.assertLessEqual(int(data['y']), int(data['map_specs']['rows']))


if __name__ == '__main__':
    unittest.main(verbosity=0)


    # dictToSend = self.map_specs
    # res = requests.post('http://localhost:5555/api/strain/map', json=self.map_specs)
    # print('response from server:', res.text)
    # dictFromServer = res.json()
    # mpeta = json.dumps(self.map_specs)