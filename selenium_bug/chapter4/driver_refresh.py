from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

driver.find_element_by_name("q").send_keys("selenium")
driver.refresh()
sleep(3)

driver.quit()