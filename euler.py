from functools import reduce

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
    return reduce((lambda x, y: x + y ),(filter(lambda x: x % 2 == 0,(i for i in fib_gen(4000000)))))
