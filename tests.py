import unittest
import euler

class Test_euler_answers(unittest.TestCase):

    def test_multiples_of_three_and_five(self):
        """Project Euler problem 1: test that the sum of multiples of three and five return correct number"""
        self.assertEqual(euler.multiples_of_three_and_five(10), 23)
        self.assertEqual(euler.multiples_of_three_and_five(1000), 233168)

    def test_fibonacci_generator(self):
        """test to see if a fibonacci sequence is generated"""
        fib_sequence = [i for i in euler.fib_gen(10)]
        self.assertEqual(fib_sequence,[1,1,2,3,5,8])
    
    def test_even_fibonacci_numbers(self):
        """Project Euler problem 2: test the sum of all even fibonacci numbers below 4 000 000"""
        self.assertEqual(euler.even_fibonacci_numbers(4000000),4613732)
 
    def test_is_prime(self):
        """test that number is prime"""
        self.assertTrue(euler.is_prime(7))

    def test_prime_gen(self):
        prime_list = euler.prime_gen(100)
        self.assertEqual(prime_list,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])

    def test_prime_factor_gen(self):
        """test that valid prime factors are generated"""
        prime_factors = [i for i in euler.prime_factor_gen(13195)]
        self.assertEqual(prime_factors,[5,7,13,29])

    def test_largest_prime_factor(self):
        """Project Euler problem 3: test the largest prime factor of 600851475143"""
        self.assertEqual(euler.largest_prime_factor(600851475143),6857)
    
    def test_is_palindrome(self):
        """Basic palindrome test"""
        self.assertTrue(euler.is_palindrome(1001))

    def test_largest_palindrome_product_two_3digit_numbers(self):
        """Project Euler problem 4: find the largest palindrom number made from the product of two 3 digit numbers"""
        number = euler.get_largest_palindrome(100, 999)
        self.assertEqual(number,906609)

    def test_smallest_number_evenly_divisible(self):
        """Project Euler problem 5: find the smallest number divisible by all numbersbetween 1 and 20"""
        number = euler.get_smallest_divisible(1,20)
        self.assertEqual(number,232792560)

if __name__ == '__main__':
    unittest.main()
