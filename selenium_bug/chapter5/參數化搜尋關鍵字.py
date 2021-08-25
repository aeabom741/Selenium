from selenium import webdriver
from time import sleep

texts = ["selenium",'python','RobotFramework']

for text in texts:

    driver = webdriver.Chrome()
    driver.get("https://www.google.com.tw/")
    
    search = driver.find_element_by_xpath("//input[@name='q']")
    search.send_keys(text)
    search.submit()
    sleep(3)
    driver.quit()