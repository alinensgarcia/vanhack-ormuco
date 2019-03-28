from crawler import Crawler
from content_analyzer import get_most_relevant_contents

class ResultsExtractor():
    def __init__(self, search_topic):
        self.search_topic = search_topic
        self.most_relevant_contents = []

    def extract_results():
        'results: Most relevant contents from top 5 search results.'
        
        self.most_relevant_contents = get_most_relevant_contents(
                            Crawler(self.search_topic).get_contents())

    