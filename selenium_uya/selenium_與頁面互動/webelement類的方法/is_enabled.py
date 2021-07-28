from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get("file:///Users/lvjiawei/Documents/Be%20stronger/code/Selenium/selenium_uya/selenium_%E8%88%87%E9%A0%81%E9%9D%A2%E4%BA%92%E5%8B%95/test.html")
driver.maximize_window()

username = driver.find_element_by_xpath("//input[@name='username']")
password = driver.find_element_by_xpath("//input[@name='password']")

print("username is enable:{0}".format(username.is_enabled()))
print("password is enable:{0}".format(password.is_enabled()))

driver.quit()