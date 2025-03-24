import os
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, cenario, id_test, step_name):
        """Captura o print da tela e salva com o nome do step"""
        # Define o diretório onde as capturas de tela serão salvas
        folder_name = os.path.join('Screenshot', cenario, id_test)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Cria o caminho do arquivo baseado no step_name
        timestamp = time.strftime("%Y%m%d_%H%M%S")  # Adiciona timestamp para evitar sobrescrita
        screenshot_path = os.path.join(folder_name, f"{step_name}_{timestamp}.png")
        
        # Captura a tela
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot salva em: {screenshot_path}")

    def enter_iframe(self, iframe: WebElement):
        """Entra em um iframe"""
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        print("Entrou no iframe.")

    def exit_iframe(self):
        """Sai do iframe e volta para o conteúdo principal"""
        self.driver.switch_to.default_content()
        print("Saiu do iframe.")