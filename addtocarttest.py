from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import json
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

driver.get("http://zabee-env.jsmhwy6kip.us-east-1.elasticbeanstalk.com/login")

username = driver.find_element_by_id("l_user_email")
username.clear()
username.send_keys("qa5.kaygees@gmail.com")


password = driver.find_element_by_id("l_user_pass")
password.clear()
password.send_keys("admin123")

driver.find_element_by_id("join-us-btn").click()

#SEARCH_INPUT2 = (By.XPATH, "//div[@class='row']/div[@class='col-sm-12 product-accessories carousel slide']/div[@class='position-relative']/div[@class='carousel-inner']/div[@class='carousel-item active']/div[@class='card-deck m-1']/div[4]/div[@class='polaroid']/div[@class='image-center-parent']/a[2]")
    #/div[@class='polaroid']
#driver.find_element(SEARCH_INPUT2).click()

#search_input = driver.find_element_by_xpath("//div[@class='image-center-parent']/button[@class='btn cart-buttons addToWishlistBtn btn-left']").click()
search_input = driver.find_element_by_xpath("//div[@class='image-center-parent']/a[@class='btn cart-buttons btn-right addToCartBtn']").click()
search_input.text.click()
#search_input.click()
driver.implicitly_wait(10)
driver.quit()