from unittest import TestCase
from app import app

class TestApp(TestCase):
    def setUp(self):
        self.search_topic = 'keystone - Circular reference found role inference'
        self.app = app.test_client()

    def test_get_relevant_results(self):
        response = self.app.get('/relevant_results/' + self.search_topic)
        self.assertEqual(200, response.status_code)
        
    def test_unsupported_search_topic(self):
        response = self.app.get('/relevant_results/NOT {}'.format(
                                                            self.search_topic))
        self.assertEqual(response.get_data(), b'Search topic not supported yet.')

    def test_get_empty_search_topic(self):
        response = self.app.get('/relevant_results/')
        self.assertEqual(404, response.status_code)