
import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    #initialize driver instance
    b = selenium.webdriver.Chrome("C:\chromedriver")
    #driver = webdriver.Chrome("C:\chromedriver")
    #driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')


    #wait 10 seconds to let page load
    b.implicitly_wait(10)

    #return webdriver instance
    yield b
    
    #Quit webdriver instance
    b.quit()