import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class ClickSelect(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://goodstartbook.com/pruebas/")

    def test1(self):
        elemento = driver.find_element_by_xpath("//div[@id='center']/button")
        if elemento is not None:
            elemento.click()
        alerta = driver.switch_to_alert
        time.sleep(3)
        alerta.accept()    
        #time.sleep(3)
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
