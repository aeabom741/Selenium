from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/bing_iframe.html')
driver.switch_to_frame(0)
driver.find_element_by_xpath("//input[@id='sb_form_q']").send_keys("selenium")

# 重要
driver.switch_to_default_content()
# 重要
driver.find_element_by_xpath("//input[@id='userid']").send_keys("selenium")
sleep(3)
driver.quit()