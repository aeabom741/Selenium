from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

search = driver.find_element_by_name("q")
search.send_keys("selenium")
sleep(3)

driver.quit()