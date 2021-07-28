from logging import PlaceHolder
from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get("file:///Users/lvjiawei/Documents/Be%20stronger/code/Selenium/selenium_uya/selenium_%E8%88%87%E9%A0%81%E9%9D%A2%E4%BA%92%E5%8B%95/test.html")

username = driver.find_element_by_xpath("//input[@name='username']")
password = driver.find_element_by_xpath("//input[@name='password']")

print("用戶名:{0}".format(username.get_attribute('PlaceHolder')))
print("密碼:{0}".format(password.get_attribute('placeHolder')))

driver.quit()