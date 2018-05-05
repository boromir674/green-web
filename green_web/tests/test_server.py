import requests
import os
import sys
import json
import unittest
import tempfile
from green_web import green_app

d = dict(columns=20,
         grid='rectangular',
         initialization='pca',
         rows=10,
         type='toroid'
    )


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        # self.db_fd, green_app.config['DATABASE'] = tempfile.mkstemp()
        green_app.testing = True
        self.app = green_app.test_client()
        self.strain_id = 'amnesia'
        self.map_specs = {
            'columns': 5,
            'grid': 'rectangular',
            'initialization': 'pca',
            'rows': 7,
            'type': 'toroid'
        }
        self.ms0 = {'rows': 10}
        self.ms = d
        self.map_specs2 = b'{"columns": 20, "grid": "rectangular", "initialization": "pca", "rows": 10, "type": "toroid"}'
        # TODO decouple the 'new-dt' component of the id
        self.map_id = 'somoclu_new-dt_pca_toroid_rectangular_7_5'
        # self.map_id2 = "somoclu_new-dt_pca_toroid_rectangular_20_10"
        # with green_app.app_context():
        #     flaskr.init_db()

    def tearDown(self):
        pass
        # os.close(self.db_fd)
        # os.unlink(flaskr.app.config['DATABASE'])

    def test_strain_id_endpoint(self):
        response = self.app.get('/api/strain/'+self.strain_id)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('flavors', data)
        self.assertIn('name', data)
        self.assertIn('type', data)
        self.assertEqual(data['flavors'], ['Earthy', 'Sweet', 'Pungent'])
        self.assertEqual(data['name'], 'amnesia')
        self.assertEqual(data['type'], 'sativa')

    def test_map_creation_endpoint(self):
        dictToSend = self.map_specs
        res = requests.post('http://localhost:5555/api/strain/map', json=dictToSend)
        print('response from server:', res.text)
        dictFromServer = res.json()
        # response = self.app.post('/api/strain/map', data=self.ms0, follow_redirects=True)
        # data = json.loads(response.get_data(as_text=True))
        self.assertIn('map_id', dictFromServer)
        self.assertEqual(dictFromServer['map_id'], self.map_id)


if __name__ == '__main__':
    unittest.main(verbosity=0)
