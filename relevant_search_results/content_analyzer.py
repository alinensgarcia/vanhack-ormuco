import json

class ContentAnalyzer():
    def get_relevant_contents(self, dict_html_pages):        
        '''
        Return relevant content as above:

        relevant_contents = {
            'url': ['paragraph', 'code_snippet', 'comment'],
            'url2': ['paragraph', 'paragraph2', 'code_snippet', 'code_snippet2'],
            ...
        }
        '''

        relevant_contents = {}
        for url, html in dict_html_pages.items():
            if 'github' in url:
                relevant_contents[url] = self.__get_list_page_contents(
                                                                html, '//td')
            else:
                relevant_contents[url] = (
                    self._extract_relevant_paragraphs(html) + \
                    self._extract_code_snippets(html)
                )

        return relevant_contents


    def _extract_code_snippets(self, html):
        '''return: ['content1', 'content2']'''

        pre_code = self.__get_list_page_contents(html, '//pre//code')
        pre = self.__get_list_page_contents(html, '//pre')

        return pre_code + pre

    def _extract_relevant_paragraphs(self, html):
        return self.__get_list_page_contents(html, '//p')

    def __get_list_page_contents(self, html_page, xpath_str):
        elements = html_page.xpath(xpath_str)
        contents = []

        # returns text content with lenght greater than 5 (arbitrary rule)
        for e in elements:
            if len(e.text_content()) > 5:
                contents.append(e.text_content().replace('\t','').strip())
        
        return contents