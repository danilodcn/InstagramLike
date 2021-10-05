from Instagram.Pages.Search import SearchPage
from Instagram.Pages.Home import Home
from .Pages.Login import Login
from collections import namedtuple
from json import load
from configparser import ConfigParser
import pickle


def create_name_tuple(dic: dict):
    values = []
    keys = []

    def convert_for_tuple(lst: list):
        if isinstance(lst, tuple):
            # import ipdb; ipdb.set_trace()
            try:
                keys = lst._fields
                e_namedtuple = True
            except:
                e_namedtuple = False
                # raise ValueError("Aqui")
            
            values = []

            for value in lst:
                if isinstance(value, (list, dict)):
                    value = convert_for_tuple(value)
                values.append(value)
            
            if e_namedtuple:
                Tabela = namedtuple("Tabela", keys)
                return Tabela(*values)
            else:
                return tuple(values)

        if isinstance(lst, list):
            return tuple(
                [convert_for_tuple(x) for x in lst]
            )
        elif isinstance(lst, dict):
            return create_name_tuple(lst)
        return lst

    for key, value in dic.items():
        # if key == "nome":
        #     import ipdb; ipdb.set_trace()

        if isinstance(value, dict):
            value = create_name_tuple(value)
        
        elif isinstance(value, list):
            value = tuple(value)
        try:
            int(key)
            key = "a_" + str(key)
        except ValueError:
            ...
        keys.append(key)
        values.append(convert_for_tuple(value))

    Tabela = namedtuple("Tabela", keys)
    tabela = Tabela(*values)
    return tabela


class Instagram:
    def __init__(self, webdriver, urls={}):
        self.webdriver = webdriver
        self._pages = {"Login": 6}
        if urls == {}:
            with open("./Instagram/urls.json") as file:
                self.urls = load(file)
        else: 
            self.urls = urls

        self.config = ConfigParser()
        self.config.read("./config.ini")
        # import ipdb; ipdb.set_trace()
    
    def create_pages(self):
        # print("Criando")
        pages = {}
        login_url = self.urls["login"]
        user_password = dict(self.config.items("user.login")).values()
        pages["Login"] = Login(self.webdriver, login_url, *user_password)

        pages["Home"] = Home(self.webdriver, url=self.urls["home"])

        pages["Search"] = SearchPage(self.webdriver)

        self.Pages = create_name_tuple(pages)

    def save_section(self):
        with open("cookies.pkl", "wb") as file:

            pickle.dump(self.webdriver.get_cookies(), file)

    def load_section(self):
        self.webdriver.get(self.urls["home"])
        with open("./cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                self.webdriver.add_cookie(cookie)
        
        self.webdriver.get(self.urls["home"])
        # import ipdb; ipdb.set_trace()

