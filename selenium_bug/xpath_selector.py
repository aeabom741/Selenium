from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

#element selector (xpath)
search = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
search_button = driver.find_element_by_xpath("//input[@class='gNO89b']")
good_hand = driver.find_element_by_xpath("//input[@class='RNmpXc']")

#element
search_name = search.get_attribute("name")
search_button_value = search_button.get_attribute("value")
good_hand_value = good_hand.get_attribute("value")

print(search_name)
print(search_button_value)
print(good_hand_value)

driver.quit()