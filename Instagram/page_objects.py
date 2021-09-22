from abc import ABC
from selenium import webdriver
from selenium.webdriver import Firefox as WebDriver


class SeleniumObjetc:
    def find_element(self, locator):
        return self.webdriver.find_element_by(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements_by(*locator)


class Page(ABC, SeleniumObjetc):
    def __init__(self, webdriver: WebDriver, url=""):
        self.webdriver = webdriver
        self.url = url
        self._reflection()

    def open(self, url=""):
        if url:
            self.webdriver.get(url)
        else:
            self.webdriver.get(self.url)

    def _reflection(self):
        for attr in dir(self):
            real = getattr(self, attr)
            if isinstance(real, PageElement):
                real.webdriver = self.webdriver


class PageElement(ABC, SeleniumObjetc):
    def __init__(self, webdriver: WebDriver=None):
        self.webdriver = webdriver