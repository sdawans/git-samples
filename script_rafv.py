from cash_register import CashRegister
from calculator import Calculator
import pprint

cash_register = CashRegister()
calculator = Calculator()

change = cash_register.compute_change(40, 1)
pprint.pprint(change)
calculator.wall(1,2)