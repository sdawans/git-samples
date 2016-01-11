from calculator import Calculator
from primeperfib import Calculator
from cash_register import CashRegister
import pprint

calc = Calculator()
ppf = PrimePerFib()
cash_register = CashRegister()

change = cash_register.compute_change(1000, 2000)
pprint.pprint(change)
