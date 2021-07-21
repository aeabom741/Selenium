from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw")
buttom = driver.find_element_by_partial_link_text("關於")
buttom.click()
print(driver.title)

driver.quit()

