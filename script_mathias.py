from calculator import Calculator
from primeperfib import PrimePerFib
from cash_register import CashRegister
import pprint

calc = Calculator()
ppf = PrimePerFib()
cash_register = CashRegister()

change = cash_register.compute_change(300,200)


ran = calc.rand()

print "test"
print "hotfix336"
print("rand:%d" % (ran))
pprint.pprint(change)
