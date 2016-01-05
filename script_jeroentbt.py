from calculator import Calculator
from primeperfib import PrimePerFib
from cash_register import CashRegister
import pprint
import argparse

calc = Calculator()
ppf = PrimePerFib()
cash_register = CashRegister()

parser = argparse.ArgumentParser()
parser.add_argument('due', type=float)
parser.add_argument('paid', type=float)

args = parser.parse_args()


change = cash_register.compute_change(args.due, args.paid)
pprint.pprint(change)
