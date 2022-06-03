def factorial(number: int) -> int:
    """
    Calculate the factorial of the input `number` (denoted !number in mathematics) , which is the result of multiplying all decimal number from 1 to `number`
    e.g: factorial(5) = 1*2*3*4*5 = 120

    :param number: An integer to calculate factorial result
    :return: The factorial result. Return 1 if `number` equals 0
    """
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i

        return result


for number in range(0, 10):
    print(f"{number} {factorial(number)}")
