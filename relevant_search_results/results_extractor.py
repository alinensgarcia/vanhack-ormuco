from crawler import GoogleCrawler, SiteCrawler
from content_analyzer import ContentAnalyzer

class ResultsExtractor():
    def __init__(self, search_topic):
        self.search_topic = search_topic

    def get_relevant_contents(self):
        'results: Most relevant contents from top 5 search results.'
        try:
            return ContentAnalyzer().get_relevant_contents(
                                        self._get_html_pages())
        except:
            raise Exception('An error occurred while extracting relevant content')

    def _get_html_pages(self):
        '''returns: dict -> {'link': HtmlElement}
        '''
        links = GoogleCrawler(self.search_topic).get_top5_links()
        return SiteCrawler(links).get_html_pages()