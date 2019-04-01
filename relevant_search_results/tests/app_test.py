from unittest import TestCase
from app import app

class TestApp(TestCase):
    def setUp(self):
        self.search_topic = 'keystone - Circular reference found role inference'
        self.app = app.test_client()

    def test_get_relevant_results(self):
        response = self.app.get('/relevant_results/' + self.search_topic)
        self.assertEqual(200, response.status_code)
        
        # print(response.data)
        
    # def test_get_empty_search_topic(self):
    #     search_topic = ''
    #     # get('/relevant-search-results/api/v1.0/results/<search_topic>')
    #     pass