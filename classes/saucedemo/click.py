from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestClick:
    def __init__(self, driver):
        self.driver = driver

    def click_products(self, path_element):
        element = self.driver.find_element(By.XPATH, path_element)
        element.click()
        time.sleep(1)