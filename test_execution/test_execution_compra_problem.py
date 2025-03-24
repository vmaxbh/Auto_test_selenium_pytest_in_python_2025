import pytest
from tests.id02_compra_problem.id06_login import Teste06CenariosLogin
from tests.id02_compra_problem.id07_product import Teste07EscolhaProduto
#from tests.id02_compra_problem.id08_checkout import Teste08Checkout
from tests.id02_compra_problem.id09_logout import Teste09LogOut


class TestExecutionCompraProblem:
    def test_execution(self):
        Teste06CenariosLogin().__init__()
        Teste07EscolhaProduto().__init__()
        #Teste08Checkout().__init__()
        Teste09LogOut().__init__()
        
        