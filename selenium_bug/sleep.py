from selenium import webdriver
from time import ctime,sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

print(ctime())
search = driver.find_element_by_xpath("//input[@name='q']")
search.send_keys("selenium")
sleep(2)
search.submit()
print(ctime())

driver.quit()