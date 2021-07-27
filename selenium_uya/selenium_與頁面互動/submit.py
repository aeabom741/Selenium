from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///Users/lvjiawei/Documents/Be%20stronger/code/Selenium/selenium_uya/selenium_%E8%88%87%E9%A0%81%E9%9D%A2%E4%BA%92%E5%8B%95/From.html")

driver.find_element_by_xpath("//input[@name='username']").send_keys("selenium")
driver.find_element_by_name("form").submit()
t.sleep(2)
driver.quit()