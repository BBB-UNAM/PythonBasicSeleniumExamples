import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://goodstartbook.com/pruebas/")

    def testId(self):
        elementById = driver.find_element_by_id("noImportante")
        if elementById is not None:
            print("Encontramos el elemento con Id = noImportante")

    def testName(self):
        elementByName = driver.find_element_by_name("ultimo")
        if elementByName is not None:
            print("Encontramos el elemento con name = ultimo")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
