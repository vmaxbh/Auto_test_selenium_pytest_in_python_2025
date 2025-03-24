import pytest
from selenium import webdriver
from classes.saucedemo.login import LoginPage
from classes.saucedemo.credencials import Credenciais
from classes.base_class import BaseClass

cenario = "01_Compra_Sauce_Labs_BackPack"
id_test = "test_01"

class Teste01:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        """Inicializa o driver e a página de login."""
        self.driver = browser
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)

    def test_login_sucesso(self):
        """Testa o login bem-sucedido."""
        step = "step_1"
        self.login_page.acessar_site()
        self.login_page.fazer_login(Credenciais.USUARIO_CORRETO, Credenciais.SENHA_CORRETA)
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        assert "inventory" in self.driver.current_url, "Login falhou!"

    def test_login_invalido(self):
        """Testa o login inválido."""
        step = "step_2"
        self.login_page.acessar_site()
        self.login_page.fazer_login(Credenciais.USUARIO_ERRADO, Credenciais.SENHA_ERRADA)
        mensagem_erro = self.login_page.obter_mensagem_erro()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        assert "Epic sadface" in mensagem_erro, "Mensagem de erro não apareceu corretamente!"