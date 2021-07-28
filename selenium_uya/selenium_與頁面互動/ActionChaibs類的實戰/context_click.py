from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
locator = driver.find_element_by_xpath("//input[@name='q']")
ActionChains(driver).context_click().perform()
