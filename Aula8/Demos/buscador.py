from selenium import webdriver

class Google:

    def __init__(self, url):
        self._url = url
        self._driver = webdriver.Chrome('./driver/chromedriver.exe')

    def acessa_site(self):
        self._driver.get(self._url)

    def efetua_busca(self, valor_buscado):
        self._driver.find_element_by_class_name('classe').send_keys(valor_buscado)

    def clica_botao(self):
        self._driver.find_elements_by_class_name('classe').click()
