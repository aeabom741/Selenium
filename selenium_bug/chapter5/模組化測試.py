from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.google.com.tw")

def Ig_web():
    driver.find_element_by_xpath("//input[@name='q']").send_keys("IG")
    driver.find_element_by_xpath("//input[@name='q']").submit()
    sleep(2)
    driver.find_element_by_xpath("//div[@class='yuRUbf']/a").click()

def login_Ig():
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
    inputs = driver.find_elements_by_xpath("//input[@class='_2hvTZ pexuQ zyHYP']")


    button = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
    button.click()


Ig_web()
login_Ig()
