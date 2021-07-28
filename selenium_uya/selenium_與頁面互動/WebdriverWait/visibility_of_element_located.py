from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
google = WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"關於 Google")))
google.click()
driver.quit()