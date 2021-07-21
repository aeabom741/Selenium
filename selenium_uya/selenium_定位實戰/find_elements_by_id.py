from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("file:///Users/lvjiawei/Documents/Be%20stronger/code/Selenium/selenium_uya/selenium_%E5%AE%9A%E4%BD%8D%E5%AF%A6%E6%88%B0/test_web.html")

logins = driver.find_elements_by_id("login")
for login in logins:
    print(login)

driver.find_elements_by_id("login")[0].send_keys("00000")
driver.find_elements_by_id("login")[1].send_keys("aeabom")
sleep(3)

driver.quit()