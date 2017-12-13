from functools import reduce

def multiples_of_three_and_five(n):
    """Find the sum of all the multiples of 3 or 5 below 1000."""
    return reduce((lambda x, y: x + y), (i for i in range(1,n) if i % 3 == 0 or i % 5 == 0))
