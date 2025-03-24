import pytest
from tests.id01_compra_standard.id01_login import Teste01CenariosLogin
from tests.id01_compra_standard.id02_product import Teste02EscolhaProduto
from tests.id01_compra_standard.id03_checkout import Teste03Checkout
from tests.id01_compra_standard.id04_logout import Teste04LogOut


class TestExecutionCompraStandard:
    def test_execution(self):
        Teste01CenariosLogin().__init__()
        Teste02EscolhaProduto().__init__()
        Teste03Checkout().__init__()
        Teste04LogOut().__init__()
        
        