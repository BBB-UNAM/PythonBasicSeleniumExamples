import unittest
from selenium import webdriver

class FindByIdName (unittest.TestCase):

    def setUp(self):
        global driver 
        driver = webdriver.Firefox()
        driver.get("http://goodstartbook.com/pruebas/")

    def testIdName(self):
        elementById = driver.find_element_by_id("noImportante")
        if elementById is not None:
            print("Encontramos el elemento con Id = noImportante")

        elementByName = driver.find_element_by_name("ultimo")
        if elementByName is not None:
            print("Encontramos el elemento con name = ultimo")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
