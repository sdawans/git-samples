import argparse

class CashRegister():
    """A Cash Register to Add/Remove money and compute change"""
    def __init__(self):
        self.denominations = [
                        {'value':0.01, 'type': 'coin', 'name': 'One cent'},
                        {'value':0.02, 'type': 'coin', 'name': 'Two cent'},
                        {'value':0.05, 'type': 'coin', 'name': 'Five cent'},
                        {'value':0.10, 'type': 'coin', 'name': 'Ten cent'},
                        {'value':0.20, 'type': 'coin', 'name': 'Twenty cent'},
                        {'value':0.50, 'type': 'coin', 'name': 'Fifty cent'},
                        {'value':1, 'type': 'coin', 'name': 'One Euro'},
                        {'value':2, 'type': 'coin', 'name': 'Two Euro'},
                        {'value':5, 'type': 'note', 'name': 'Five Euro'},
                        {'value':10, 'type': 'note', 'name': 'Ten Euro'},
                        {'value':20, 'type': 'note', 'name': 'Twenty Euro'},
                        {'value':50, 'type': 'note', 'name': 'Fifty Euro'},
                        {'value':100, 'type': 'note', 'name': 'One Hundred Euro'},
                        {'value':200, 'type': 'note', 'name': 'Two Hunder Euro'},
                        {'value':500, 'type': 'note', 'name': 'Five Hundred Euro'},
                        {'value':1000, 'type': 'note', 'name': 'One Thousand Euro'},
                        {'value':2000, 'type': 'note', 'name': 'Two Thousand Euro'},
                        {'value':5000, 'type': 'note', 'name': 'Five Thousand Euro'},
                        {'value':5000000, 'type': 'gem', 'name': 'Five Million Euro'},
                        ]
        self._balance = 0

    @property
    def balance(self):
        return _balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def add_amount(self, amount):
        """Add money to the cash register"""
        self.balance += amount

    def remove_amount(self, amount):
        """Remove money from the cash register"""
        self.balance -= amount

    def compute_change(self, due, paid):
        """Return a dictionary of denominations representing the change based on amounts due and paid"""
        change_value = paid - due
        denominations = self.denominations[:]
        change = []
        while denominations:
            denomination = denominations.pop()
            divisor = denomination['value']
            count = int(change_value/divisor)
            if count > 0:
                denomination['count'] = count
                change.append(denomination)
            change_value = change_value % divisor
        return change

if __name__ == '__main__':
    """When run as a script, perform change computation based on amount due and paid"""
    cash_register = CashRegister()
    parser = argparse.ArgumentParser()
    parser.add_argument('due', type=float)
    parser.add_argument('paid', type=float)

    args = parser.parse_args()

    change = cash_register.compute_change(args.due, args.paid)

    print("########################\n##### CashRegister #####\n########################\n")
    print("Amount Due: %.2f" % args.due)
    print("Amount Paid: %.2f" % args.paid)
    print("Change:")
    for elem in change:
        print(" * %d %s %s%s" % (elem['count'],elem['name'],elem['type'], 's' if elem['count'] > 1 else ''))