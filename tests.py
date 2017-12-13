import unittest
import euler

class Test_euler_answers(unittest.TestCase):

    def test_multiples_of_three_and_five(self):
        """test that the sum of multiples of three and five return correct number"""
        self.assertEqual(euler.multiples_of_three_and_five(10), 23)
        self.assertEqual(euler.multiples_of_three_and_five(1000), 233168)

    def test_fibonacci_generator(self):
        """test to see if a fibonacci sequence is generated"""
        fib_sequence = [i for i in euler.fib_gen(10)]
        self.assertEqual(fib_sequence,[1,1,2,3,5,8])
    
    def test_even_fibonacci_numbers(self):
        """test the sum of all even fibonacci numbers below 4 000 000"""
        self.assertEqual(euler.even_fibonacci_numbers(10),4613732)
    

if __name__ == '__main__':
    unittest.main()
