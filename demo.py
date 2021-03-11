from selenium import webdriver


#driver = webdriver.Chrome("C:\chromedriver")
#driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

driver.get("http:google.com")