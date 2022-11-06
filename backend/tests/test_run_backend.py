""" Unit tests for all the methods of the src.run_backend file. """
from fastapi.testclient import TestClient
from src.run_backend import app

client = TestClient(app)


def test_healthcheck(self):
    """ Unit tests for the healthcheck method. """
    response = client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), {'message': 'Jean Cloud Vinyl Backend is running.'})


def run_tests(self):
    """ Function to run all the tests for the src.run_backend methods. """
    test_healthcheck(self)
