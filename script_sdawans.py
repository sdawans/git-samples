from calculator import Calculator
from primeperfib import PrimePerFib
from cash_register import CashRegister
import pprint

calc = Calculator()
ppf = PrimePerFib()
cash_register = CashRegister()

change = cash_register.compute_change(140,120)
pprint.pprint(change)

c = calc.addanddividebytwo(10, 10)
pprint.pprint(c)