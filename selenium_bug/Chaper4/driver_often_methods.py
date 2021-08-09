from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")

#search element method
search = driver.find_element_by_name("q")
print(search.is_displayed())

search.send_keys("selenium")
search.submit()

driver.back()
sleep(2)

#other APImethod
button_value = driver.find_element_by_xpath("//div[@class='uU7dJb']")
print(button_value.get_attribute("type"))
print(button_value.text)

buttons = driver.find_elements_by_xpath("//a[@class='pHiOh']")
for button in buttons:
    print(button.get_attribute("text"))


driver.quit()