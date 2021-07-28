from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
locator = driver.find_element_by_xpath("//input[@name='q']")
locator.send_keys("selenium")
locator.send_keys(Keys.COMMAND,'a')
locator.send_keys(Keys.COMMAND,'c')
locator.clear()
t.sleep(2)
locator.send_keys(Keys.COMMAND,'v')

locator.submit()