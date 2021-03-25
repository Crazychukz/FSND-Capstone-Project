import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db

access_token=os.environ.get('ACCESS_TOKEN')


class MoviesActorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.headers = {'Authorization': access_token}
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total'])

    def test_add_movie(self):
        res = self.client().post('/movies', headers=self.headers, json={
            'title': "Test Movie",
            'release_date': "12-06-2012",
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_update_movie(self):
        res = self.client().patch('/movies/1', headers=self.headers, json={
            'title': "Test Movie 22",
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total'])

    def test_add_actor(self):
        res = self.client().post('/actors', headers=self.headers, json={
            'name': "Tom Cruise",
            'age': "45",
            'gender': "Male"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_update_actor(self):
        res = self.client().patch('/actors/1', headers=self.headers, json={
            'name': "Thomas Cruise",
            'age': "45",
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
