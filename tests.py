import unittest
import euler

class Test_euler_answers(unittest.TestCase):

    def test_multiples_of_three_and_five(self):
        self.assertEqual(euler.multiples_of_three_and_five(10), 23)
        self.assertEqual(euler.multiples_of_three_and_five(1000), 233168)


if __name__ == '__main__':
    unittest.main()
