from calculator import Calculator
from primeperfib import PrimePerFib
from cash_register import CashRegister

calc = Calculator()
ppf = PrimePerFib()
cash_register = CashRegister()

change = cash_register.compute_change(140,210)
print(change)

a=10
b=50
result = calc.bhendrickx(a,b)
print("Result of the bhendrickx(%d,%d) is %d" % (a, b, result))