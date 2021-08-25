from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Ig_test():

    def login(self, driver, username, password):
    
        #emter web
        driver.get('https://www.instagram.com/')

        #ig account login
        WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@class='_2hvTZ pexuQ zyHYP']")))
        format= driver.find_elements_by_xpath("//input[@class='_2hvTZ pexuQ zyHYP']")

        #type account
        format[0].send_keys(username)
        format[1].send_keys(password)

        #enter
        button = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
        button.click()

    def quit(self,driver):
        driver.quit()


driver = webdriver.Chrome()
Ig_test().login(driver,"aeabom741@gmail.com",'az011105')
Ig_test().quit(driver)