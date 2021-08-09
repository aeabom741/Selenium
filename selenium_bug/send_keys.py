from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

search = driver.find_element_by_name("q")
search.send_keys('selenium')

#複製
search.send_keys(Keys.COMMAND,"a")
search.send_keys(Keys.COMMAND,"c")

#清空
search.clear()
sleep(2)

#貼上
search.send_keys(Keys.COMMAND,'v')
sleep(2)

#搜尋
search.send_keys(Keys.ENTER)
sleep(2)

driver.quit()