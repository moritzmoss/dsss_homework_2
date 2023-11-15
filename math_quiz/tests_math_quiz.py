import unittest
from math_quiz import getRandomInteger, getRandomArithmeticSymbol, mathematicalOperation


class TestMathGame(unittest.TestCase):

    def test_getRandomInteger(self):
        # Test if random numbers generated are within the specified range
        minFirstOperand = 1
        maxFirstOperand = 10
        for _ in range(1000):  # Test a large number of random values
            randFirstOperand = getRandomInteger(minFirstOperand, maxFirstOperand)
            self.assertTrue(minFirstOperand <= randFirstOperand <= maxFirstOperand)

        minSecondOperand = 1
        maxSecondOperand = 5
        for _ in range(1000):  # Test a large number of random values
            randSecondOperand = getRandomInteger(minSecondOperand, maxSecondOperand)
            self.assertTrue(minSecondOperand <= randSecondOperand <= maxSecondOperand)

    def test_getRandomArithmeticSymbol(self):
        # Test if random arithmetic symbols generated are within the predefined once
        for _ in range(1000):  # Test a large number of random values
            randArithmeticSymbol = getRandomArithmeticSymbol()
            self.assertIn(randArithmeticSymbol, ['+', '-', '*'])

    def test_mathematicalOperation(self):
        # Test if specific test cases results in correct mathematical equation and output
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 2, '-', '2 - 2', 0),
                (10, 1, '*', '10 * 1', 10),
                (4, 1, '+', '4 + 1', 5),
                (2, 5, '-', '2 - 5', -3),
                (5, 2, '*', '5 * 2', 10),
                (9, 3, '*', '9 * 3', 27),
                (7, 2, '+', '7 + 2', 9),
                (9, 2, '-', '9 - 2', 7),
                (5, 1, '-', '5 - 1', 4)
            ]

            for firstOperand, secondOperand, operator, expected_problem, expected_answer in test_cases:
                # Test each single test case for correctness
                problem, answer = mathematicalOperation(firstOperand, secondOperand, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
