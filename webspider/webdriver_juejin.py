# filename: webspider.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://www.juejin.im")
input = browser.find_element_by_css_selector(".search-input")
input.send_keys('node')
input.send_keys(Keys.ENTER)


