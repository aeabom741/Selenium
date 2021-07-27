from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw")

print("頁面代碼：{0}".format(driver.page_source))
driver.quit()