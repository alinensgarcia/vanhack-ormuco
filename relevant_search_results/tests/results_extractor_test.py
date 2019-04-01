from unittest import TestCase
from results_extractor import ResultsExtractor
import json


class TestResultsExtractor(TestCase):
    def setUp(self):
        self.search_topic = 'keystone - Circular reference found role inference'

    def test_extract_results(self):
        # ResultsExtractor(self.search_topic)
        rc = ResultsExtractor(self.search_topic).get_relevant_contents()
        relevant_contents = json.loads(rc)
        
        for url, relevant_content in relevant_contents.items():
            self.assertIn('http', url)
            self.assertNotEqual(len(relevant_content), 0)