import pytest
from selenium import webdriver
from classes.saucedemo.login import LoginPage
from classes.saucedemo.credencials import Credenciais
from classes.saucedemo.click import TestClick
from classes.saucedemo.navigate import TestNavigate
from classes.saucedemo.input import TestFillData
from classes.base_class import BaseClass

cenario = "01_Compra_Sauce_Labs_BackPack"
id_test = "test_04"

class Teste04LogOut:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.driver = browser 
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)
        self.click = TestClick(self.driver)  
        self.nav = TestNavigate(self.driver)
        self.input = TestFillData(self.driver)
    
    def test_logout(self):
        step = "step_1"
        self.login_page.acessar_site()
        self.login_page.fazer_login(Credenciais.USUARIO_CORRETO, Credenciais.SENHA_CORRETA)
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_2"
        self.nav.navigate_logout_action_logout()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        
       
        

    
        
