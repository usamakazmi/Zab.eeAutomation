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
    
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title



############################################################################################################
############################################################################################################
class DuckDuckGoSearchPage:
    
    #url
    URL = 'https://duckduckgo.com/'

    #locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    #initializer
    def __init__(self, browser):
        self.browser = browser

    #interaction methods
    def load(self):
        self.browser.get(self.URL)

    def search(self,phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)


############################################################################################################
############################################################################################################
# content of test_sample.py
@pytest.mark.parametrize('phrase', ['panda','python','polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    #PHRASE = "panda"

    search_page.load()

    search_page.search(phrase)
    
    #WebDriverWait(search_page, 10).until(EC.title_contains(phrase))
    
    #time.sleep(5)
    #search result query is "panda"
    
    assert phrase == result_page.search_input_value()

    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0


    #add the search result
    assert phrase in result_page.title()
   