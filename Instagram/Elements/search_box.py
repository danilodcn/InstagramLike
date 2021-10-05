from re import search
from typing import List

from selenium.webdriver.common.by import By
from Instagram.page_objects import PageElement
from selenium.webdriver import Firefox as WebDriver


class SearchBox(PageElement):
    def __init__(self, webdriver: WebDriver = None):
        super().__init__(webdriver=webdriver)
        

    def search_by_terms(self, terms: List[str], numeros: List[int] = 10):

        hrefs = {}
        if isinstance(numeros, int):
            numeros = [numeros] * len(terms)

        for term, n in zip(terms, numeros):
            result = self.search_by_term(term, n)
            hrefs[term] = list(result)
        
        self.log("Todas as urls foram capturadas", "info")
        return hrefs
    
    def search_by_term(self, term, n=5):
        locator = By.XPATH, "//input[@placeholder]"
        self.search_box = self.find_element(locator)

        # import ipdb; ipdb.set_trace()
        self.search_box.clear()
        self.search_box.send_keys(term)

        locator = By.XPATH, "//div[@role='none']"
        self.wait_while_load(locator)
        self.sleep(.1)

        locator = By.XPATH, "//div[@aria-hidden='false']//a"
        
        elements = self.find_elements(locator)
        if len(elements) > n:
            elements = elements[: n]
        self.log(f'Urls da busca {term} capturadas com sucesso', "info")
        for element in elements:

            yield element.get_attribute("href")
            # import ipdb; ipdb.set_trace()

        