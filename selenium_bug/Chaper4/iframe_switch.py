from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/frame.html")


driver.switch_to_frame(0)
search = driver.find_element_by_xpath("//input[@name='q']")
for i in range(10):
    if search.is_displayed():
        search.send_keys("selenium")
        break
    else:
        print("element not found")
sleep(2)
driver.quit()