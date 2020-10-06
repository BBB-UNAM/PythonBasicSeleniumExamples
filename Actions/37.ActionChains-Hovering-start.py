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
        iFrameID = driver.find_element_by_id("pruebas-iframe")
        if iFrameID is not None:
            driver.switch_to.frame(iFrameID)
        nombre = driver.find_element_by_id("Segundo")
        if nombre is not None:
            nombre.send_keys("Juan")
           
        time.sleep(3)
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
