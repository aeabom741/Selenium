from selenium import webdriver
from time import sleep

drive = webdriver.Chrome()
drive.get("https://www.google.com.tw/")

#select element
search = drive.find_element_by_class_name("gNO89b")
good_hand = drive.find_element_by_class_name("RNmpXc")

#get elemnt value
search_value = search.get_attribute("value")
good_hand_value = good_hand.get_attribute("value")

#print value
print(search_value)
print(good_hand_value)

drive.quit()