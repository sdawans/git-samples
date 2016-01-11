from calculator import Calculator
from primeperfib import PrimePerFib
from cash_register import CashRegister
import pprint

calc = Calculator()
ppf = PrimePerFib()
cash_register = CashRegister()

change = cash_register.compute_change(140, 210)
pprint.pprint(change)

result = calc.add(1, 3)
print(result)

powpowresult = calc.powpow(5,2)
print("Result of the powpow(5,2) is %d" % powpowresult)
