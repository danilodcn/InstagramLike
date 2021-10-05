from selenium.webdriver.common import keys
from Instagram.page_objects import Page
from Instagram.Elements.search_box import SearchBox
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Home(Page):
    def __init__(self, webdriver: WebDriver, url=""):
        super().__init__(webdriver, url=url)

        self.SearchBox = SearchBox(self.webdriver)
    
    
