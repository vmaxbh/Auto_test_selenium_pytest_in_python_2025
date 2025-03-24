from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from classes.saucedemo.click import TestClick
import time


class TestNavigate:
    def __init__(self, driver):
        self.driver = driver
        self.click = TestClick(self.driver)

    def navigate_checkout_action_checkout(self):
        self.click.click_products("//a[@class='shopping_cart_link']")
        self.click.click_products("//button[@id='checkout']")

    def navigate_logout_action_logout(self):
        self.click.click_products("//button[@id='react-burger-menu-btn']")
        self.click.click_products("//a[@id='logout_sidebar_link']")

