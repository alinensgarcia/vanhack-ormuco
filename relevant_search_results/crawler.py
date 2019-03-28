class Crawler():
    def __init__(self, search_topic):
        self.search_topic = search_topic
        self.contents = []

    def get_contents(links):
        links = GoogleCrawler().links_google_top5_results(
                    self.search_topic)
        
        # for link in links:
        #   self.contents.append(SiteCrawler.get_content(link))
        return self.contents


class GoogleCrawler():
    def links_google_top5_results(search_topic):
        # links = scrapy ...
        # return links
        pass


class SiteCrawler():
    def get_content(link):
        # content = scrapy...(link)
        # return content
        pass