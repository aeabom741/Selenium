from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

search = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,"q")))
search.send_keys("selenium")

driver.quit()