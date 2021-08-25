from selenium import webdriver
from time import sleep,ctime

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/checkbox.html")
sleep(2)

inputs = driver.find_elements_by_tag_name("input")
print("總共有幾個checkbox:",len(inputs))
for input in inputs:
    if input.get_attribute("type") == 'checkbox':
        input.click()
        sleep(2)

driver.quit()