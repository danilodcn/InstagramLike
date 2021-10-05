from selenium.webdriver.common import keys
from Instagram.page_objects import Page
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login(Page):
    def __init__(self, webdriver: WebDriver, url="", user="", password=""):
        super().__init__(webdriver, url=url)
        self.user = user
        self.password = password

    def login(self):
        self.open()
        locator = By.XPATH, "//button"
        self.wait_while_load(locator, .5, "Login carregando", "info")
        locator = By.NAME, "username"
        login = self.find_element(locator)
        login.send_keys(self.user)

        self.sleep()

        locator = By.NAME, "password"
        password = self.find_element(locator)
        password.send_keys(self.password)

        password.send_keys(Keys.ENTER)

        self.save_info_and_turn_of_notifications()
        

    def save_info_and_turn_of_notifications(self):
        locator = By.XPATH, "//a/*[name()='svg']"
        self.wait_while_load(locator)

        self.sleep(.2)
        self.save_info()
        # import ipdb; ipdb.set_trace()

        self.turn_of_notifications()

    def save_info(self):
        locator = By.XPATH, "//button[@type='button']"
        save_info = self.find_element(locator)
        save_info.click()
        # import ipdb; ipdb.set_trace()

    def turn_of_notifications(self):
        locator = By.XPATH, "//div/img[@alt='']"
        self.wait_while_load(locator, .5, "Esperando carregar a tela notificações")
        self.sleep(3)
        self.wait_while_load(locator, .5, "notificações carregadas")
        self._turn_of_notifications()

    def _turn_of_notifications(self):
        locator = By.XPATH, "//div/button[@tabindex=0 and not( @role)]"
        notifications = self.find_elements(locator)[1]
        
        notifications.click()
    