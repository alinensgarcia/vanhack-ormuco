from unittest import TestCase
from crawler import _get_page_html
from content_analyzer import ContentAnalyzer
import json


class ContentAnalyzerTest(TestCase):
    def setUp(self):
        self.urls = ['https://bugs.launchpad.net/bugs/1803780',
        'https://bugs.launchpad.net/bugs/1780224',
        'https://docs.openstack.org/keystone/pike/_modules/keystone/assignment/core.html',
        'http://tarballs.openstack.org/translation-source/keystone/master/keystone/locale/keystone-log-error.pot',
        'https://github.com/Vincit/objection.js/issues/787']

        self.html_pages = dict()
        for url in self.urls:
            self.html_pages[url] = _get_page_html(url)

    def test_get_relevant_content(self):
        json_relevant_contents = ContentAnalyzer().get_relevant_contents(
                                    self.html_pages)
        relevant_contents = json.loads(json_relevant_contents)
        
        for url, relevant_content in relevant_contents.items():
            self.assertIn('http', url)
            self.assertNotEqual(len(relevant_content), 0)