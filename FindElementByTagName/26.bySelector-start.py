import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://goodstartbook.com/pruebas/")

    def testId(self):
        elementById = driver.find_element_by_link_text("Pagina 2")
        if elementById is not None:
            print("Encontramos el elemento con texto Pagina 2")

    def testName(self):
        elementByName = driver.find_element_by_partial_link_text("agina")
        if elementByName is not None:
            print("Encontramos el elemento usando texto parcial")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
