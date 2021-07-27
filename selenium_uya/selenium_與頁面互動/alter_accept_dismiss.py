from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time as t

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/alert.html")
button =  driver.find_element_by_xpath("//input[@type='button']")
button.click()
t.sleep(2)

driver.switch_to_alert().dismiss()
t.sleep(2)