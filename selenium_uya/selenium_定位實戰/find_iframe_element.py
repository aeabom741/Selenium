from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/frame.html')

driver.switch_to_frame(0)

text = driver.find_element_by_xpath('/html/body').text
print(text)

driver.quit()
