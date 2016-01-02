"""
This is an adaptation and annotated version of code originally found here:
http://code.activestate.com/recipes/577229-prime-perfect-and-fibonacci-number-widget-class/
"""

class PrimePerFib:
    """Generate and manipulate Prime, Perfect and Fibonacci Numbers"""
    def __init__(self):
        pass

    def gen_factor(self, n):
        """Generate all the factors of a number"""
        l1, l2 = [], []
        for i in range(1, int(n ** 0.5) + 1):
            q,r = n//i, n%i
            if r == 0:
                l1.append(i)
                l2.append(q)
        if l1[-1] == l2[-1]:
            l1.pop()
        l2.reverse()
        for prime in (l1 + l2):
            yield prime
            
    def is_prime(self, n):
        for x in self.gen_factor(n):
            if x != 1 and x != n:
                return False
        return True

    def prime_gen(self, count, start):
        """Generate a sequence of prime numbers

        Arguments:
            count: The number of prime numbers to generate
            start: The start of the sequence
        """
        c     = 0
        base  = [2,3,5]
        start = int(round(start))
              
        n = (2,max(2,(start,start+1)[start % 2 == 0]))[start != 2]
        
        while c < count:
                  
            if n in base:
                yield n
                if n == 2: n+=1; c+=1; continue
                else: n+=2; c+=1; continue
                
            if not [m for m in base if (n%60) % m == 0 ]:
                if n % n**0.5 != 0:
                    if self.is_prime(n):
                        c += 1
                        yield n
            n += 2

    def prime_get(self, num):
        """Get the next prime number starting at and incluing the input value"""
        r = self.prime_gen(count=1,start=num).next()
        return r

    def prime_next(self, num):
        """Get the next prime number starting at and not incluing the input value"""
        return self.prime_get(num+1)

    def perfect_gen(self, count, start=0):
        """Generate a sequence of perfect numbers

        Arguments:
            count: The number of perfect numbers to generate
            start: The start of the sequence, defaults to 0
        """
        output = 0
        prime  = 0 
        while output < count:
            prime = self.prime_next(prime)
            mPrime = 2**prime - 1

            if not self.is_prime(mPrime):
                continue
            
            pN =(2**(prime-1))*(2**prime - 1)
            if pN >= start:
                output += 1
                yield pN
                    
    def perfect_get(self, num):
        """Get the next perfect number starting at and incluing the input value"""
        return self.perfect_gen(count=1,start=num).next()

    def is_perfect(self, num):
        """Check if the input value is a perfect number"""
        return self.perfect_get(num)==num

    def perfect_next(self, num):
        """Get the next perfect number starting at and not incluing the input value"""
        return self.perfect_get(num+1)

    def fibonacci_gen(self, count, start=0):
        """Generate a sequence of fibonacci numbers

        Arguments:
            count: The number of fibonacci numbers to generate
            start: The start of the sequence, defaults to 0
        """
        output = 0
        fib    = [0,1]
        while output < count:
            fN = fib[len(fib)-1] + fib[len(fib)-2]
            fib.append(fN)
            fib.pop(0)
            if fN >= start:
                output += 1
                yield fN

    def fibonacci_get(self, num):
        """Get the next fibonacci number starting at and incluing the input value"""
        return self.fibonacci_gen(count=1,start=num).next()

    def is_fibonacci(self, num):
        """Check if the input value is a fibonacci number"""
        return self.fibonacci_get(num)==num

    def fibonacci_next(self, num):
        """Get the next fibonacci number starting at and not incluing the input value"""
        return self.fibonacci_get(num+1)

if __name__ == '__main__':
    
    PPF = PrimePerFib()
    
    ##########################################################################
    #Prime Numbers
    
    print "What Prime Number Comes After 56? ",PPF.prime_next(56)
    print "Is 333 A Prime Number? ",PPF.is_prime(333)

    Primes = []
    for Prime in PPF.prime_gen(count=10,start=42):
        Primes.append(Prime)
        
    print "Generated Primes: ",Primes,"\n\n"
    
    ##########################################################################
    #Perfect Numbers
    #Need Some Horsepower In Your Machine To Play With These
    
    print "What Perfect Number Comes After 9685 ",PPF.perfect_next(9685)
    print "Is 8128 A Perfect Number ",PPF.is_perfect(8128)
    
    Perfects = []
    for Perfect in PPF.perfect_gen(count=8, start=0):
        Perfects.append(Perfect)
        
    print "Generated Perfect Numbers ",Perfects,"\n\n"
    
    ##########################################################################
    #Fibonacci Numbers
    
    print "What is the Next Fibonacci Number After 5 ? ",PPF.fibonacci_next(5)
    print "Is 16 A Fibonacci Number? ",PPF.is_fibonacci(16)
    
    Fibonaccis = []
    for Fibonacci in PPF.fibonacci_gen(count=42, start=10):
        Fibonaccis.append(Fibonacci)
        
    print "Generated Fibonacci Numbers ",Fibonaccis
        
    
