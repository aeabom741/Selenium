from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")
search = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
search.send_keys("selenium")

WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@class='gNO89b']")))
click_btn = driver.find_element_by_xpath("//input[@class='gNO89b']")
click_btn.click()

driver.quit()