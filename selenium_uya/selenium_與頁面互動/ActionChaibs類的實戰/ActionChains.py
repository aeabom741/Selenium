from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
driver.find_element_by_xpath("//a[@class='gb_C']").click()

driver.switch_to_frame(0)
locator = driver.find_element_by_link_text("搜尋")
ActionChains(driver).move_to_element(locator).click().perform()
