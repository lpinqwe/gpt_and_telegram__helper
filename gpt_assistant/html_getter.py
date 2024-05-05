from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


class HTMLGetter:
    browser = None

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Enable headless mode
        self.browser = webdriver.Chrome(options=chrome_options)

    def __del__(self):
        self.close_browser()

    def close_browser(self):
        if self.browser is not None:
            self.browser.quit()

    def get_html(self, url):
        self.browser.get(url)
        html = self.browser.page_source
        time.sleep(2)
        return html


test_url = "https://www.pracuj.pl/praca/c%252B%252B%20programmer"
test = HTMLGetter()
print(test.get_html(test_url))
