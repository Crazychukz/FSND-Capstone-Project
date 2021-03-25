import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db

access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFVWkRSVE5DTWpZNU5UTXhOMFE1TWpFM01ETTVPVFExTmpjMFF6Z" \
               "EVOVEU0TkVFelF6VXhOdyJ9.eyJpc3MiOiJodHRwczovL2NyYXp5Y2h1a3ouYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aD" \
               "J8MTE0MDkyOTE4Nzg5OTcyMTc4MDA0IiwiYXVkIjpbImNjbS1jb2ZmZWUiLCJodHRwczovL2NyYXp5Y2h1a3ouYXV0aDAuY29tL3VzZ" \
               "XJpbmZvIl0sImlhdCI6MTYxNDU0MzE1MCwiZXhwIjoxNjE0NTUwMzUwLCJhenAiOiJwSVdXSU9lc053RzFiZXliNVE5VkpxdVdjMHhN" \
               "SE9BRyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5" \
               "rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.GNcAqx9V2qAERZb9pQIYdwYX_9B-ekJh4QfEBoEPhZDh7" \
               "0Q2EKHpMyG0NUetY_fuku1e5gsgYXz2N7URWC-LN0NCYpA_Muyz948qZc7FkURFUXhq5H2FEajEXWrTPSFXV5Fvj4AGZiUS6Ajdbwnw" \
               "-J03amBc7eugnQnBIccNp-BZbPJMa4lnKOssuJtjQB6aRbyCnrKVvguYQnI_stH97XNVcC0-YGTdTAODFLGTzwNu38NH7xQQso_MyYv" \
               "Lq-OOpgugAG4U3zUmc_m9b9I_fwhReVczk4J60LssUw7Dfz5qX625YzrnDc1echMHXPVtqJIkg9jWvW3U-uE-hhc7VA"


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
