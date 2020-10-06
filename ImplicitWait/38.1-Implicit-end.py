import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class Espera(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)
    
        driver.get("http://goodstartbook.com/pruebas/")

    def test1(self):
        boton = driver.find_element_by_id("proceed")
        if boton is not None:
            boton.click()
           
        time.sleep(3)
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
