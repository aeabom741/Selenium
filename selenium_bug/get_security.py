from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

#login 
driver.find_element_by_link_text("登入").click()
print(driver.title)

#username
username = driver.find_element_by_xpath("//input[@id='identifierId']")
username.send_keys("aeabom741@gmail.com")

#login button
button = driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']")
button.click()

sleep(2)

#login info
info = driver.find_element_by_xpath("//h1[@id='headingText']")
print("登錄資訊:"+ info.text)

if info.text == "目前無法登入帳戶":
    print("brower error!!")

driver.quit()