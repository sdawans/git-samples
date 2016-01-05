import argparse

class Calculator():
    """A basic calculator, little more than a wrapper for some basic arithmetic operators."""

    def __init__(self):
        self.choices_cmd = ['add', 'sub', 'mul', 'div', 'pow', 'mod', 'floor']

    def add(self, op1, op2):
        """Add the two input arguments."""
        return op1 + op2

    def sub(self, op1, op2):
        """Subtract the two input arguments."""
        return op1 - op2

    def mul(self, op1, op2):
        """Multiply the two input arguments."""
        return op1 * op2

    def div(self, op1, op2):
        """Divide the two input arguments."""
        return op1 / op2

    def pow(self, op1, op2):
        """Raise the first argument to the power of the second argument."""
        return op1 ** op2

    def mod(self, op1, op2):
        """Take the modulo of the first argument by the second argument."""
        return op1 % op2

    def floor(self, op1, op2):
        """Make a floor division of the first argument by the second argument."""
        return op1 // op2

    def bhendrickx(self, op1, op2):
        return op1 / 100 + op2 / 100

if __name__ == '__main__':
    """When run as a script, perform an operation based on an input operator and operands
    and print the results in standard output.
    """
    calc = Calculator()
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=calc.choices_cmd)
    parser.add_argument('operand1')
    parser.add_argument('operand2')
    args = parser.parse_args()

    method = getattr(calc, args.command)
    result = method(float(args.operand1), float(args.operand2))

    print("########################\n###### Calculator ######\n########################\n")
    print("Operator: %s" % args.command)
    print("Operands: %f %f" % (float(args.operand1), float(args.operand2)))
    print("Result: %2.2f" % result)
