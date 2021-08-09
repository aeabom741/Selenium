from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

search = driver.find_element_by_xpath("//input[@name='q']")
search.send_keys("selenium")

ActionChains(driver).context_click(search).perform()

driver.quit()