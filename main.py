from Instagram.Instagram import Instagram
from selenium.webdriver import Firefox, Chrome

driver = Firefox()
instagram = Instagram(driver)
# instagram.load_section()
instagram.create_pages()
instagram.Pages.Login.login()
# instagram.Pages.Login.turn_of_notifications()
terms = ["cursos online", "arduino cursos", "matemática aplicada", "egenharia eletrica"]
urls = instagram.Pages.Home.SearchBox.search_by_terms(terms, 6)
urls = ['https://www.instagram.com/cursonline.br/', 'https://www.instagram.com/aluraonline/']
_urls = instagram.Pages.Search.by_urls(urls)
instagram.Pages.Search.like_comments(_urls)


instagram.save_section()

import ipdb; ipdb.set_trace()
driver.quit()