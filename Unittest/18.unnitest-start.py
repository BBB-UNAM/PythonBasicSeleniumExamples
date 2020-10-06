from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://goodstartbook.com/pruebas/")

elementById = driver.find_element_by_id("noImportante")
if elementById is not None:
    print("Encontramos el elemento con Id = noImportante")

elementByName = driver.find_element_by_name("ultimo")
if elementByName is not None:
    print("Encontramos el elemento con name = ultimo")

driver.quit()

#unittest.main()
