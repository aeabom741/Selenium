from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

commercial = driver.find_element_by_partial_link_text("廣告")
ActionChains(driver).move_to_element(commercial).click().perform()
