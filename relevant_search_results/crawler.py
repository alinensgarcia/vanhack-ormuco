from lxml import html
import requests
import re
import logging


class GoogleCrawler():
    def __init__(self, search_topic):
        try:
            self.url = 'https://www.google.com/search?q=' + search_topic
        except:
            raise Exception('An error occurred while crawling Google results')

    def get_top5_links(self):
        try:
            page_html = _get_page_html(self.url)
            google_search_items = _get_page_html(self.url).xpath('//h3/a/@href')
            google_search_links_list = [re.search('q=(.*)&sa', i).group(1) 
                                        for i in google_search_items][:5]
            return google_search_links_list
        except:
            raise Exception('An error occurred while crawling Google results')
  
class SiteCrawler():
    def __init__(self, links):
        self.links = links
    
    def get_html_pages(self):
        htmls_dict = {}
        try:
            for site_url in self.links:
                htmls_dict[site_url] = _get_page_html(site_url)
            return htmls_dict
        except:
            raise Exception('An error occurred while crawling site content')

def _get_page_html(url):
    page = requests.get(url)
    return html.fromstring(page.content)