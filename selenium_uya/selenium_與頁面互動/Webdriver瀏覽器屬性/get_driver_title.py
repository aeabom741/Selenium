from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw")

print("當前頁面標籤:{0}".format(driver.title))
driver.quit()