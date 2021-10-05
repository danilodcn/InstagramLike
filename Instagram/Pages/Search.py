from typing import List
from Instagram.page_objects import Page
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage(Page):
    def __init__(self, webdriver: WebDriver, url="", urls=[]):
        super().__init__(webdriver, url=url)
    
    def like_comments(self, urls, numeros=10):
        if isinstance(numeros, int):
            numeros = [numeros] * len(urls)

        for url, n in zip(urls, numeros):
            self.like_comment(url, n)

    def like_comment(self, url, n=10):
        self.log(f"Fazendo os comentários da página {self.webdriver.title}", "info")
        import ipdb; ipdb.set_trace()
        self.open(url)


    def by_urls(self, urls: List=[]):
        _urls = set()
        # import ipdb; ipdb.set_trace()
        
        for url in urls:
            links = self.by_url(url)
            _urls.update(links)

        return _urls

    def by_url(self, url: str, n=10):
        urls = set()
        self.open(url=url)
        locator = By.XPATH, "//article//a"
        self.wait_while_load(locator)
        self.sleep(.5)
        
        while len(urls) < n:
            element = self.find_element(locator)
            element.send_keys(Keys.CONTROL + Keys.DOWN)
            self.sleep(.5)
            elements = self.find_elements(locator)
            links = map(lambda elem: elem.get_attribute("href"), elements)
            urls.update(links)
            # import ipdb; ipdb.set_trace()

        # import ipdb; ipdb.set_trace()

        return urls
