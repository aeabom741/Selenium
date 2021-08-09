from selenium import webdriver
from time import sleep

driver= webdriver.Chrome()
driver.get("https://www.google.com.tw/")

driver.maximize_window()
sleep(2)
driver.set_window_size(400,600)
sleep(2)
driver.quit()