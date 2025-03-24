import pytest
from selenium import webdriver
from classes.saucedemo.login import LoginPage
from classes.saucedemo.credencials import Credenciais
from classes.saucedemo.click import TestClick
from classes.base_class import BaseClass

cenario = "05_select_full_products_visual_true"
id_test = "test_14"

class Teste14SelectProduct:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.driver = browser 
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)
        self.click = TestClick(self.driver)  

    def test_products_select(self):
        self.login_page.acessar_site()
        self.login_page.fazer_login(Credenciais.USUARIO_VISUAL, Credenciais.SENHA_CORRETA)
        step = "step_1"
        self.click.click_products("//button[@id='add-to-cart-sauce-labs-backpack']")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_2"
        self.click.click_products("//button[@id='add-to-cart-sauce-labs-bike-light']")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_3"
        self.click.click_products("//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_4"
        self.click.click_products("//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_5"
        self.click.click_products("//button[@id='add-to-cart-sauce-labs-onesie']")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_6"
        self.click.click_products("//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        










        

    
        
