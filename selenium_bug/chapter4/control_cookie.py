from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/")
for cookie in driver.get_cookies():
    print("%s : %s" %(cookie['name'],cookie['value']))

driver.quit()