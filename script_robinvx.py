from calculator import Calculator
from primeperfib import PrimePerFib
from cash_register import CashRegister

calc = Calculator()
ppf = PrimePerFib()
cash_register = CashRegister()

change = cash_register.compute_change(140, 210)
pprint.pprint(change)

