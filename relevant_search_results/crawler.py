from lxml import html
import requests
import re
import logging


class GoogleCrawler():
    def __init__(self, search_topic):
        self.url = 'https://www.google.com/search?q=' + search_topic

    def get_top5_links(self):
        google_search_items = _get_page_html(self.url).xpath('//h3/a/@href')
        google_search_links_list = [re.search('q=(.*)&sa', i).group(1) 
                                    for i in google_search_items][:5]
        return google_search_links_list

  
class SiteCrawler():
    def __init__(self, links):
        self.links = links
    
    def get_html_pages(self):
        htmls_dict = {}

        for site_url in self.links:
            # print('Crawling site: ' + site_url)
            htmls_dict[site_url] = _get_page_html(site_url)
            
        # for k,v in htmls_dict.items():
        #     print(k, v)

        return htmls_dict


def _get_page_html(url):
    page = requests.get(url)
    return html.fromstring(page.content)