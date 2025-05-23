import pytest
from selenium import webdriver
from classes.saucedemo.login import LoginPage
from classes.saucedemo.credencials import Credenciais
from classes.saucedemo.click import TestClick
from classes.base_class import BaseClass

cenario = "02_Compra_Sauce_Labs_bolt_t_shirt"
id_test = "test_07"

class Teste07EscolhaProduto:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.driver = browser 
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)
        self.click = TestClick(self.driver)  

    def test_products_select(self):
        step = "step_1"
        self.login_page.acessar_site()
        self.login_page.fazer_login(Credenciais.USUARIO_PROBLEM, Credenciais.SENHA_CORRETA)
        step = "step_2"
        self.click.click_products("//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_3"
        self.click.click_products("//button[@data-test='add-to-cart']")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)

    
        
