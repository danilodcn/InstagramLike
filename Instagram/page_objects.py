from abc import ABC
from selenium import webdriver
from selenium.webdriver import Firefox as WebDriver
from traceback import print_exc
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import logging


def get_logger(name = "Log", *args):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("log.log")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

logger = get_logger()
logger_level = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
    }

class SeleniumObjetc:
    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

    def wait_while_load(self, locator, _time=.5, log_msg="", level="info"):
        get_out = False
        while not get_out:
            # import ipdb; ipdb.set_trace()
            self.sleep(_time)
            if log_msg:
                self.log(log_msg, level)

            try:
                element = self.find_element(locator)
                get_out = True
            except NoSuchElementException:
                # print_exc()
                pass
            
    def sleep(self, _time=.1):
        sleep(_time)

    @staticmethod
    def log(msg, level="info", *args):
        logger.log(logger_level[level], msg)


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