from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

driver.find_element_by_link_text("關於 Google").click()
sleep(2)

driver.quit()