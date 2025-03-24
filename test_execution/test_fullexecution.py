import pytest
from tests.id01_compra_true.id01_login import Teste01
from tests.id01_compra_true.id02_product import Teste02
from tests.id01_compra_true.id03_checkout import Teste03
from tests.id01_compra_true.id04_logout import Teste04
from tests.id02_compra_problem.id06_login import Teste06
from tests.id02_compra_problem.id07_product import Teste07
from tests.id02_compra_problem.id08_checkout import Teste08
from tests.id02_compra_problem.id09_logout import Teste09
from tests.id03_compra_visual_true.id10_login import Teste10
from tests.id03_compra_visual_true.id11_product import Teste11
from tests.id03_compra_visual_true.id12_checkout import Teste12
from tests.id03_compra_visual_true.id13_logout import Teste13
from tests.id04_select_products_visual_true.id14_product import Teste14
#from tests.id05_select_products_true.id15_product import Teste15
#from tests.id06_select_products_problem.id16_product import Teste16



class TestExecutionFull:
    def test_execution(self):
        Teste01().__init__()
        Teste02().__init__()
        Teste03().__init__()
        Teste04().__init__()
        Teste06().__init__()
        Teste07().__init__()
        Teste08().__init__()
        Teste09().__init__()
        Teste10().__init__()
        Teste11().__init__()
        Teste12().__init__()
        Teste13().__init__()
        Teste14().__init__()
        #Teste15().__init__()
        #Teste16().__init__()