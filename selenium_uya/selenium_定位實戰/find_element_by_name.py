from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw")

search = driver.find_element_by_name('q')
search.send_keys("news")

click_btn = driver.find_element_by_name("btnK")
click_btn.click()
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,'q')))
driver.quit()