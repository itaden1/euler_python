import unittest
import euler

class Test_euler_answers(unittest.TestCase):

    def test_multiples_of_three_and_five(self):
        self.assertEqual(euler.multiples_of_three_and_five(10), 23)
        self.assertEqual(euler.multiples_of_three_and_five(1000), 233168)

    def test_even_fibonacci_numbers(self):
        self.assertEqual(euler.even_fibonacci_numbers(10),44)
        self.assertEqual(euler.even_fibonacci_numbers(4000000),44)

if __name__ == '__main__':
    unittest.main()
