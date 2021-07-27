from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://google.com.tw')
t.sleep(2)
driver.quit()