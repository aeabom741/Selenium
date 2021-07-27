from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com.tw")

print('測試網址為:{0}'.format(driver.current_url))
driver.quit()