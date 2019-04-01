from unittest import TestCase

class TestApp(TestCase):
    def setUp(self):
        self.search_topic = 'Testes Automatizados'

    def test_get_results(self):
        # self.search_topic
        # get('/relevant-search-results/api/v1.0/results/<search_topic>')
        pass

    # def test_get_empty_search_topic(self):
    #     search_topic = ''
    #     # get('/relevant-search-results/api/v1.0/results/<search_topic>')
    #     pass