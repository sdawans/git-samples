from cash_register import CashRegister
import pprint

cash_register = CashRegister()

change = cash_register.compute_change(40, 1)
pprint.pprint(change)