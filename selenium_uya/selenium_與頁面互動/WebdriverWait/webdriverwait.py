from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
driver.maximize_window()


driver.find_element_by_xpath("//input[@name='q']").send_keys("selenium")

WebDriverWait(driver,10,0.5).until(EC.element_to_be_clickable((By.XPATH,"//input[@class='gNO89b']")))
driver.find_element_by_xpath("//input[@class='gNO89b']").click()

t.sleep(3)
driver.quit()