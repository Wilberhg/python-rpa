from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

#driver = webdriver.Chrome(r'C:\Users\Wilber Godoy\Downloads\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(r'.\chromedriver.exe')

driver.maximize_window()
driver.implicitly_wait(30)

driver.get('https://google.com.br')
driver.find_element_by_class_name('gLFyf.gsfi').send_keys('Python')
driver.find_element_by_class_name('gNO89b').click()
driver.find_element_by_class_name('LC20lb.DKV0Md').click()
driver.find_element_by_link_text('Downloads').click()
driver.find_element_by_link_text('Download Python 3.10.0').click()
