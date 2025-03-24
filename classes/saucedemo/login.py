from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, browser):
        self.driver = browser
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[contains(text(), 'Epic sadface: Username and password do not match any user in this service')]")

    def acessar_site(self):
        """Acessa o site da Sauce Demo"""
        self.driver.get("https://www.saucedemo.com/")
        print("Site acessado: https://www.saucedemo.com/")

    def fazer_login(self, usuario, senha):
        """Faz login com o usuário e senha fornecidos"""
        # Aguarda até que o campo de nome de usuário esteja visível
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field))
        self.driver.find_element(*self.username_field).send_keys(usuario)
        
        # Aguarda até que o campo de senha esteja visível
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field))
        self.driver.find_element(*self.password_field).send_keys(senha)
        
        # Aguarda até que o botão de login esteja visível antes de clicar
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        self.driver.find_element(*self.login_button).click()
        print(f"Login realizado com usuário: {usuario}")

    def obter_mensagem_erro(self):
        """Obtém a mensagem de erro de login"""
        # Espera que a mensagem de erro esteja visível
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message))
        mensagem = self.driver.find_element(*self.error_message).text
        print(f"Mensagem de erro obtida: {mensagem}")
        return mensagem

    def verificar_login_sucesso(self):
        """Verifica se o login foi bem-sucedido"""
        return "inventory" in self.driver.current_url