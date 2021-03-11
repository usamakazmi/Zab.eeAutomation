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
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions
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

    b.maximize_window()
    #wait 10 seconds to let page load
    b.implicitly_wait(config['implicit_wait'])

    #return webdriver instance
    yield b
    
    #Quit webdriver instance
    #b.close()
    b.quit()




############################################################################################################
############################################################################################################
class DuckDuckGoSearchPage:
    
    #url
    URL = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/login'
    URL2 = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/account'
    URL3 = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com'
    URL4 = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/cart'
    URL5 = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/checkout?c=1'
    URL6 = 'http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/checkout/payment'
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
    
    def gotohomepage(self):
        self.browser.get(self.URL3)

    def addtocartCheck(self):
        self.browser.get(self.URL3)

    def addtowishlistCheck(self):
        self.browser.get(self.URL3)

    def gotocartpage(self):
        self.browser.get(self.URL4)
    
    def gotoshippingpage(self):
        self.browser.get(self.URL5)

    def gotopaymentpage(self):
        self.browser.get(self.URL6)


    def search(self,phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
    
    def search2(self,phrase2):
        search_input2 = self.browser.find_element(*self.SEARCH_INPUT2)
        search_input2.send_keys(phrase2 + Keys.RETURN)
    


############################################################################################################
############################################################################################################
class DuckDuckGoResultPage:
    
    #SEARCH_INPUT = (By.ID, 'accountsidebarCollapse')
    #SEARCH_INPUT = (By.CLASS_NAME, 'flipBtn sidebar-dropdown-toggle')
    #SEARCH_INPUT = (By.CSS_SELECTOR, "h4.col-4")
    #SEARCH_INPUT2 = (By.XPATH, "//a[@href='http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/orders']")
    
#THis tag is used to check if user is logged in or not
    isloggedin = (By.XPATH, "//div[@class='row mb-3']/h4[@class='col-4']")
    
    productvalue = (By.XPATH, "//div[@class='product-container ']/div[@class='row text-center ']/div[@class='col-sm-12 top-rated-product-price']")
    addtocartbutton = (By.XPATH, "//div[@class='image-center-parent']/a[@class='btn cart-buttons btn-right addToCartBtn']")
    
    addtowishlistbutton = (By.XPATH, "//div[@class='image-center-parent']/button[@class='btn cart-buttons addToWishlistBtn btn-left']")
    addtowishlistmodal = (By.XPATH, "//body[@class='page_home modal-open']/div[@class='modal fade show']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer']/button[@class='btn btn-success ml-3']")
    addtowishlistexit = (By.XPATH, "//body[@class='page_home modal-open']/div[@class='modal fade show']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-header']/button[@class='close']")

    gotoproductdetailpage  = (By.XPATH, "//div[@class='image-center-parent']/a[@class='btn cart-buttons ']/img[@class='img img-fluid mx-auto  my-auto image-center pro_img']")
    isonproductdetailpage = (By.XPATH, "//div[@class='row breadcrumb-row']/div[@class='col-sm-12 pl-3 p-2']/span[1]/a[@class='breadcrumb-link-pre-color']")
    
    addtocartonproductdetailpage = (By.XPATH, "//div[@class='row']/div[@class='col-sm-3 rightmost-div border-left-for-extreme-right-div']/div[@class='row']/div[@class='col-sm-12 pt-3 pb-3']/div[@class='row button-center']/a[@class='btn btn-hover color-orange btn-xl']")
    
    opencartsidebar = (By.XPATH, "//div[@class='flip-card-back']/a[contains (text(), 'Cart' ) ]")
    openusersidebar = (By.XPATH, "//div[@class='flip-card-back']/a[@class='flipBtn sidebar-dropdown-toggle']")
    
    gotocheckoutusingsidebarcart = (By.XPATH, "//div[@class='minicart']/a[2]/input[@value='Checkout']")
    isoncheckoutpage = (By.XPATH, "//div[@class='row breadcrumb-row']/div[@class='col-sm-12 pl-3 p-2']/span[1]/a[contains (text(), 'Home' ) ]")
    
    iswhereoncheckoutpage = (By.XPATH, "//div[@class='row breadcrumb-row']/div[@class='col-sm-12 pl-3 p-2']/span[1]/a[@class='breacrumb-latter-color']")
    findnextbutton = (By.XPATH, "//a[contains (text(), 'Next' ) ]")
    

    def __init__(self, browser):
        self.browser = browser

    #This function checks if user is logged in or not
    def loginTest(self):
        search_input = self.browser.find_element(*self.isloggedin)
        #value = search_input.find_element(*self.SEARCH_INPUT2)
        #search_input = self.browser.findElement(By.xpath("//div[@class='row mb-3']/h4[@class='col-4']")
        #self.browser.execute_script("window.history.go(-1)")
        return search_input.text

    def addtocartTest(self):
        search_input = self.browser.find_element(*self.addtocartbutton)
        search_input.send_keys(Keys.RETURN)
        #search_input.text.click()
        search_input = self.browser.find_element(*self.productvalue)
        return search_input.text
    
    def addtowishlistTest(self):
        search_input = self.browser.find_element(*self.addtowishlistbutton)
        search_input.send_keys(Keys.RETURN)
        
        #search_input = self.browser.find_element_by_css_selector('.modal-footer > button[class="btn btn-success ml-3"]/text()')
        search_input = self.browser.find_element(*self.addtowishlistmodal)
        search_input.send_keys(Keys.RETURN)
        
        temp = self.browser.find_element(*self.addtowishlistexit)
        temp.send_keys(Keys.RETURN)
        
        return search_input.text
   
    def gotoproductdetailpageTest(self):
        search_input = self.browser.find_element(*self.gotoproductdetailpage)
        ActionChains(self.browser).move_to_element(search_input).click().perform()  
        search_input = self.browser.find_element(*self.isonproductdetailpage)
        return search_input.text
    #this does nothing right now but might be useful in the future
    def find(self):
        search_input = lambda: self.browser.find_element(*self.addtocartonproductdetailpage)
        if search_input:
            return search_input
        else:
            return False

    def addtocartonproductdetailpageTest(self):
        #self.browser.implicitly_wait(30)
        #search_input = WebDriverWait(self.browser, 20).until(find)
        #this sleep is crucial
        time.sleep(1)
        search_input = self.browser.find_element(*self.addtocartonproductdetailpage)
        ActionChains(self.browser).move_to_element(search_input).click().perform()  
        #search_input.send_keys(Keys.RETURN)
        return search_input.text

    def opencartsidebarTest(self):
        search_input = self.browser.find_element(*self.opencartsidebar)
        ActionChains(self.browser).move_to_element(search_input).click().perform()
        #time.sleep(1)

    def openusersidebarTest(self):
        search_input = self.browser.find_element(*self.openusersidebar)
        ActionChains(self.browser).move_to_element(search_input).click().perform()
        #time.sleep(1)
   
    def gotocheckoutusingsidebarcartTest(self):
        search_input = self.browser.find_element(*self.gotocheckoutusingsidebarcart)
        #ActionChains(self.browser).move_to_element(search_input).click().perform()
        search_input.send_keys(Keys.RETURN)
        
        search_input = self.browser.find_element(*self.isoncheckoutpage)
        #time.sleep(1)
        #return search_input.get_attribute("value")
        return search_input.text


    def confirmorderoncheckoutpageTest(self):

        search_input = self.browser.find_element(*self.iswhereoncheckoutpage)
        
        if search_input.text == "Checkout":
            search_input = self.browser.find_element(*self.findnextbutton)
            search_input.send_keys(Keys.RETURN)
            time.sleep(1)
            search_input = self.browser.find_element(*self.findnextbutton)
            search_input.send_keys(Keys.RETURN)

            return "Checkout"

        elif search_input.text == "Payment":
            search_input = self.browser.find_element(*self.findnextbutton)
            search_input.send_keys(Keys.RETURN)

            return "Payment"

        else:
            return "Confirm"
            
        

 
    def onshippingpageclicknextbuttonTest(self):
        search_input = self.browser.find_element(*self.findnextbutton)
        search_input.send_keys(Keys.RETURN)
        
        search_input = self.browser.find_element(*self.findnextbutton)
        search_input.send_keys(Keys.RETURN)
        



    def title(self):
        return self.browser.title


############################################################################################################
############################################################################################################
#WebDriverWait(search_page, 10).until(EC.title_contains(phrase))
    
    #time.sleep(5)
    #search result query is "panda"
    
# Main function that calls all the test case functions
#, phrase
#@pytest.mark.parametrize('phrase1', ['qa5.kaygees@gmail.com','qa6.kaygees@gmail.com','qa7.kaygees@gmail.com',
#'qa8.kaygees@gmail.com', 'qa9.kaygees@gmail.com','qa10.kaygees@gmail.com'])
#@pytest.mark.parametrize('phrase1', ['qa5.kaygees@gmail.com','qa6.kaygees@gmail.com'])
def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    #PHRASE = "panda"
#These are the login Credentials
    phrase1 = 'qa5.kaygees@gmail.com'
    phrase2 = 'admin123'
    search_page.load()
    
#Inserting login credentials and Logging in
    search_page.search(phrase1)
    search_page.search2(phrase2)
    

#Adding the first possible product to cart
    temp = result_page.addtocartTest()
    assert temp[0] == "$"
    browser.implicitly_wait(10)   
    search_page.gotohomepage()
  

#Goto shipping page and click next button
    search_page.gotoshippingpage()
    result_page.onshippingpageclicknextbuttonTest()
    