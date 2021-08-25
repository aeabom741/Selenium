from selenium import webdriver
from time import ctime, sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

search = driver.find_element_by_xpath("//input[@name='q']")

print(ctime())
for i in range(10):
    if search.is_displayed():
        break
    else:
        print("time out")
print(ctime())

driver.quit()