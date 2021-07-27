from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw")
driver.maximize_window()

search =  driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
search.send_keys('selenium')
search.submit()
sleep(3)
print("當前網址:{0}".format(driver.current_url))
driver.back()

print('===================')
sleep(2)
print("當前網址:{0}".format(driver.current_url))

driver.quit()