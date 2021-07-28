from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://google.com.tw")
driver.maximize_window()

driver.find_element_by_link_text("登入").click()
driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']").click()

istext = WebDriverWait(driver,10,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//div[@class='o6cuMc']"),"請輸入電子郵件地址或電話"))
print("印出結果:{0}".format(istext))

driver.quit()