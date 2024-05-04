from selenium import webdriver
import time

class html_getter:
    browser=None
    def __init__(self):
        self.browser = webdriver.Firefox()
    def get_html(self,url):
        self.browser.get(url)
        html = self.browser.page_source
        time.sleep(2)
        return html
        #print(html)
"""
url="https://www.pracuj.pl/praca/c%252B%252B%20programmer"
g=html_getter()
g.get_html(url)"""