from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys('selenium')
t.sleep(2)
driver.refresh()
t.sleep(2)
driver.quit()