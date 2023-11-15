import random


def getRandomInteger(minInteger, maxInteger):
    """
    Gives random integer between certain min and max values.

    :param minInteger: Minimum possible value
    :type minInteger: int
    :param maxInteger: Maximum possible value
    :type maxInteger: int
    :return: Random value between min and max values
    :rtype: int
    """
    try:
        if minInteger < maxInteger:
            return random.randint(minInteger, maxInteger)
        else:
            raise ValueError("First argument must be less than second argument")
    except ValueError as alert:
        print(f"Error: {alert}")


def getRandomArithmeticSymbol():
    """
    Gives random arithmetic symbol.

    :return: Random arithmetic symbol of +, - or *
    :rtype: string
    """
    return random.choice(['+', '-', '*'])


def mathematicalOperation(firstOperand, secondOperand, arithmeticSymbol):
    """
    Performs a mathematical operation.

    :param firstOperand: Value of the first operand
    :type firstOperand: int
    :param secondOperand: Value of the second operand
    :type secondOperand: int
    :param arithmeticSymbol: Certain arithmetic symbol
    :type arithmeticSymbol: string
    :return: Output of mathematical operation of first and second operand
    :rtype: int
    """
    mathematicalEquation = f"{firstOperand} {arithmeticSymbol} {secondOperand}"
    if arithmeticSymbol == '+':
        output = firstOperand + secondOperand  # perform addition
    elif arithmeticSymbol == '-':
        output = firstOperand - secondOperand  # perform subtraction
    else:
        output = firstOperand * secondOperand  # perform multiplication
    return mathematicalEquation, output


def math_quiz():
    """
    Starts a math quiz game.

    :return: Personal score of math quiz game
    :rtype: string
    """
    score = 0
    targetQuota = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(targetQuota):
        firstOperand = getRandomInteger(1, 10)
        secondOperand = getRandomInteger(1, 5)
        arithmeticSymbol = getRandomArithmeticSymbol()

        PROBLEM, ANSWER = mathematicalOperation(firstOperand, secondOperand, arithmeticSymbol)
        print(f"\nQuestion: {PROBLEM}")
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except ValueError:
                print('You entered a non integer value, try again.')
                continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1  # Raise the score value
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{targetQuota}")


if __name__ == "__main__":
    math_quiz()
