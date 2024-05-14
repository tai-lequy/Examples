import unittest

class MathOperations(object):

    def math_addition(self, number_1, number_2):
        '''
        provide math addition
        number_1: first number
        number_2: second number
        return: addition of first and second numbers
        '''
        result = number_1 + number_2
        return result
#Changes in Pycharm
    def math_subtraction(self, number_1, number_2):
        '''
        provide math subtraction
        number_1: first number
        number_2: second number
        return: subtraction of first minus second numbers
        '''
        result = number_1 - number_2
        return result

class UnitTestMathOperations(unittest.TestCase):

    def test_addition(self):
        '''
        test math addition
        '''
        math_operations = MathOperations()
        result = math_operations.math_addition(2, 2)
        self.assertEqual(result, 4, "The addition should be 4")

    def test_subtraction(self):
        '''
        test math subtraction
        '''
        math_operations = MathOperations()
        result = math_operations.math_subtraction(2, 2)
        self.assertEqual(result, 0, "The subtraction should be 0")

if __name__ == "__main__":
    unittest.main()