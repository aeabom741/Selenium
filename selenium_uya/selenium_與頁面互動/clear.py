from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
search =  driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
search.send_keys('selenium')
t.sleep(2)
search.clear()
t.sleep(2)
driver.quit()