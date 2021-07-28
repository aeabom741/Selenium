from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://google.com.tw")
print("瀏覽器:{0}".format(driver.name))
driver.quit()