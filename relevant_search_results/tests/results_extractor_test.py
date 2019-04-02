from unittest import TestCase
from results_extractor import ResultsExtractor


class TestResultsExtractor(TestCase):
    def setUp(self):
        self.search_topic = 'keystone - Circular reference found role inference'

    def test_extract_results(self):
        rc = ResultsExtractor(self.search_topic).get_relevant_contents()
        
        for url, relevant_content in rc.items():
            self.assertIn('http', url)
            self.assertNotEqual(len(relevant_content), 0)

    def test_error_handling(self):
        wrong_arg = ['']
        error_msg = 'An error occurred while extracting relevant content'

        with self.assertRaises(Exception) as context:
            ResultsExtractor(wrong_arg).get_relevant_contents()

        self.assertTrue(error_msg in str(context.exception))