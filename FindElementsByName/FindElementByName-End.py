from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.goodstartbook.com/pruebas/")
elemento = driver.find_element_by_id("noImportante")
if elemento is not None:
    print("El elemento fue encontrado")

elemento = driver.find_element_by_name("ultimo")
if elemento is not None:
    print("El elemento fue encontrado usando el atributo name")
driver.quit()
