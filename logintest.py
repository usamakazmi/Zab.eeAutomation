#from pages.result import DuckDuckGoResultPage
#from pages.search import DuckDuckGoSearchPage
#from selenium import webdriver

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import json
import time
#not using
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    
############################################################################################################
############################################################################################################
@pytest.fixture
def config(scope='session'):

    with open('config.json') as config_file:
        config = json.load(config_file)
    
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def browser(config):

    #initialize driver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    #driver = webdriver.Chrome("C:\chromedriver")
    #driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')


    #wait 10 seconds to let page load
    b.implicitly_wait(config['implicit_wait'])

    #return webdriver instance
    yield b
    
    #Quit webdriver instance
    b.quit()


############################################################################################################
############################################################################################################
class DuckDuckGoResultPage:
    
    #SEARCH_INPUT = (By.ID, 'accountsidebarCollapse')
    #SEARCH_INPUT = (By.CLASS_NAME, 'flipBtn sidebar-dropdown-toggle')
    #SEARCH_INPUT = (By.CSS_SELECTOR, "h4.col-4")

    #THis tag is used to check if user is logged in or not
    SEARCH_INPUT = (By.XPATH, "//div[@class='row mb-3']/h4[@class='col-4']")
    
    #SEARCH_INPUT2 = (By.XPATH, "//a[@href='http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/orders']")
    
    def __init__(self, browser):
        self.browser = browser

    #This function checks if user is logged in or not
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        #value = search_input.find_element(*self.SEARCH_INPUT2)
        #search_input = self.browser.findElement(By.xpath("//div[@class='row mb-3']/h4[@class='col-4']")
        return search_input.text

    def title(self):
        return self.browser.title



############################################################################################################
############################################################################################################
class DuckDuckGoSearchPage:
    
    #url
    URL = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/login'
    URL2 = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/account'

    #locators
    SEARCH_INPUT = (By.ID, 'l_user_email')
    SEARCH_INPUT2 = (By.ID, 'l_user_pass')
    
    #initializer
    def __init__(self, browser):
        self.browser = browser

    #interaction methods
    def load(self):
        self.browser.get(self.URL)

    def loginCheck(self):
        self.browser.get(self.URL2)

    def search(self,phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
    
    def search2(self,phrase2):
        search_input2 = self.browser.find_element(*self.SEARCH_INPUT2)
        search_input2.send_keys(phrase2 + Keys.RETURN)
    


############################################################################################################
############################################################################################################
# content of test_sample.py
#, phrase
#@pytest.mark.parametrize('phrase1', ['qa5.kaygees@gmail.com','qa6.kaygees@gmail.com','qa7.kaygees@gmail.com',
#'qa8.kaygees@gmail.com', 'qa9.kaygees@gmail.com','qa10.kaygees@gmail.com'])
def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    #PHRASE = "panda"
#These are the login Credentials
    phrase1 = 'qa5.kaygees@gmail.com'
    phrase2 = 'admin123'
    search_page.load()
    
#Sending login credentials
    search_page.search(phrase1)
    search_page.search2(phrase2)
    
    #WebDriverWait(search_page, 10).until(EC.title_contains(phrase))
    
    #time.sleep(5)
    #search result query is "panda"
    #print(temp)
    
#Checking if user is logged in
    search_page.loginCheck()
    find = "Profile"
    temp = result_page.search_input_value()
    assert find == temp
    #print(temp)
    

   