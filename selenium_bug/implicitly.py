from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime,sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

search = driver.find_element_by_xpath("//input[@name='q']")

driver.implicitly_wait(10)

try:
    print(ctime())
    search.send_keys("selenium")
    sleep(2)

except NoSuchElementException as e:
    print(e)

finally:
    print(ctime())
    driver.quit()



