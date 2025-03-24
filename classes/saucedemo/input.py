from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from classes.saucedemo.click import TestClick
import time


class TestFillData:
    def __init__(self, driver):
        self.driver = driver
        self.click = TestClick(self.driver)

    def fill_fields_full(self, path_element, value):
        element = self.driver.find_element(By.XPATH, path_element)  
        element.send_keys(value) 
        element.send_keys(Keys.TAB)
        element.send_keys(Keys.PAGE_UP)
        time.sleep(1) 

    def fill_checkout_your_information(self, first_name, last_name, postal_code):
        self.fill_fields_full("//input[@id='first-name']", first_name)   
        self.fill_fields_full("//input[@placeholder='Last Name']", last_name) 
        self.fill_fields_full("//input[@id='postal-code']", postal_code) 
        time.sleep(1) 