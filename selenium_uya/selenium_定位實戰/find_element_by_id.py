from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3 import disable_warnings

driver = webdriver.Chrome()
driver.get("https://tw.yahoo.com/")

search = driver.find_element_by_id('header-search-input')
search.send_keys('selenium')

click_btn = driver.find_element_by_id('header-desktop-search-button')
click_btn.click()

driver.quit()
