import pytest
from selenium import webdriver
from classes.saucedemo.login import LoginPage
from classes.saucedemo.credencials import Credenciais
from classes.base_class import BaseClass

cenario = "02_Compra_Sauce_Labs_bolt_t_shirt"
id_test = "test_06"

class Teste06:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser ):
        self.driver = browser 
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)  # Passa o driver para o BaseClass

    def test_login_sucesso(self):
        step = "step_1"
        self.login_page.acessar_site()
        self.login_page.fazer_login(Credenciais.USUARIO_PROBLEM, Credenciais.SENHA_CORRETA)
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        assert "inventory" in self.driver.current_url, "Login falhou!"

    def test_login_invalido(self):
        step = "step_2"
        self.login_page.acessar_site()
        self.login_page.fazer_login(Credenciais.USUARIO_ERRADO, Credenciais.SENHA_ERRADA)
        mensagem_erro = self.login_page.obter_mensagem_erro()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        assert "Epic sadface" in mensagem_erro, "Mensagem de erro não apareceu corretamente!"
    
    
