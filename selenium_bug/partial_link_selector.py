from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

commercial = driver.find_element_by_partial_link_text("廣告")

print(commercial.get_attribute("text"))
commercial.click()
sleep(2)

driver.quit()