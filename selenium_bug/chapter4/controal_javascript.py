from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com.tw/')

search = driver.find_element_by_xpath("//input[@name='q']")
search.send_keys("selenium")
search.submit()

js = "window.scrollTo(100,600);"
driver.execute_script(js)
sleep(2)

driver.quit()