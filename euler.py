from functools import reduce
import math

def multiples_of_three_and_five(n):
    """Find the sum of all the multiples of 3 or 5 below 1000."""
    answer = reduce((lambda x, y: x + y), (i for i in range(1,n) if i % 3 == 0 or i % 5 == 0))
    return answer


def fib_gen(max_num):
    """Generates a fibonacci sequence from 0 to max_num"""
    pre,cur = 1,1
    while pre < max_num:
        yield pre
        pre,cur = cur,pre+cur        

def even_fibonacci_numbers(n):
    """By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""
    return reduce((lambda x, y: x + y ),(filter(lambda x: x % 2 == 0,(i for i in fib_gen(n)))))

def is_prime(n):
    """check if prime number"""
    if n > 1:
        if n == 2:
            return True
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    return False

def prime_gen(n):
    """Generate all primes"""
    return [x for x in range(1,n) if is_prime(x)]
    

def prime_factor_gen(n):
    """generate a prime factor sequence"""
    factors = (i for i in range(2,n) if n % i == 0 and is_prime(i))
    return [i for i in factors]

def largest_prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return max(factors)
