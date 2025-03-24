import pytest
from tests.id03_compra_visual_true.id10_login import Teste10CenariosLogin
from tests.id03_compra_visual_true.id11_product import Teste11EscolhaProduto
from tests.id03_compra_visual_true.id12_checkout import Teste12Checkout
from tests.id03_compra_visual_true.id13_logout import Teste13LogOut
from tests.id04_select_products_visual_true.id14_product import Teste14SelectProduct

class TestExecutionVisualTrue:
    def test_execution(self):
        Teste10CenariosLogin().__init__()
        Teste11EscolhaProduto().__init__()
        Teste12Checkout().__init__()
        Teste13LogOut().__init__()
        Teste14SelectProduct().__init__()
        