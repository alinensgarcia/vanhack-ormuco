from unittest import TestCase
from crawler import GoogleCrawler, SiteCrawler

class GoogleCrawlerTest(TestCase):
    def setUp(self):
        self.search_topic = 'keystone - Circular reference found role inference'

    def test_get_top5_links(self):
        links = GoogleCrawler(self.search_topic).get_top5_links()
        
        for site_url in links:
            self.assertIn('http', site_url)

        self.assertIsInstance(links, list)
        self.assertNotEqual(len(links), 0)

    def test_error_handling(self):
        wrong_arg = 0
        error_msg = 'An error occurred while crawling Google results'

        with self.assertRaises(Exception) as context:
            GoogleCrawler(wrong_arg).get_top5_links()

        self.assertTrue(error_msg in str(context.exception))


class SiteCrawlerTeste(TestCase):
    
    def setUp(self):
        self.links = ['https://bugs.launchpad.net/bugs/1803780',
        'https://bugs.launchpad.net/bugs/1780224',
        'https://docs.openstack.org/keystone/pike/_modules/keystone/assignment/core.html',
        'http://tarballs.openstack.org/translation-source/keystone/master/keystone/locale/keystone-log-error.pot',
        'https://github.com/Vincit/objection.js/issues/787']

    def test_get_html_pages(self):
        SiteCrawler(self.links).get_html_pages()

    def test_error_handling(self):
        wrong_arg = 0
        error_msg = 'An error occurred while crawling site content'

        with self.assertRaises(Exception) as context:
            SiteCrawler(wrong_arg).get_html_pages()

        self.assertTrue(error_msg in str(context.exception))