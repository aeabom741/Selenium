from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time as t

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/alert_text.html")

btn = driver.find_element_by_xpath("//input[@type='button']")
btn.click()

driver.switch_to_alert().send_keys("Leowei")
t.sleep(2)
driver.switch_to_alert().accept()
t.sleep(2)
driver.quit()