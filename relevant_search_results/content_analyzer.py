import json

class ContentAnalyzer():
    def get_relevant_contents(self, dict_html_pages):
        'return: {link: relevant_content}'
        
        relevant_contents = {}
        for url, html in dict_html_pages.items():

            if 'github' in url:
                relevant_content = self.__extract_text_from_html_element(
                                            html, '//td')
            else:
                # extract relevant paragraphs
                relevant_content = self._extract_relevant_paragraphs(html)
                
                # extract code snipetts
                relevant_content += self._extract_code_snippets(html)
                
            relevant_contents[url] = relevant_content

        json_relevant_contents = json.dumps(relevant_contents, indent=4)
        return json_relevant_contents


    def _extract_code_snippets(self, html):
        pre_code = self.__extract_text_from_html_element(html, '//pre//code')
        text = 'CODE SNIPPETS:\n'

        if len(pre_code) > 0:
            text += pre_code
        else:
            text += self.__extract_text_from_html_element(html, '//pre')

        return text


    def _extract_relevant_paragraphs(self, html):
        text = 'PARAGRAPHS:\n'
        return text + self.__extract_text_from_html_element(html, '//p')


    def __extract_text_from_html_element(self, html_page, xpath_str):
        elements = html_page.xpath(xpath_str)
        text = ''

        # returns text content with lenght greater than 5 (arbitrary rule)
        for e in elements:
            if len(e.text_content()) > 5:
                text += '{}\n'.format(e.text_content())

        return text