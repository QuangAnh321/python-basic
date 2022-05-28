def fizz_buzz(number: int) -> str:
    """
    A game that take an input `number` and return a word based on the whether the `number` is divisible by 3,
    5 both or neither

    :param number: A valid decimal number
    :return: "fizz buzz" if `number` is divisible by both 3 and 5, "fizz" if `number` is divisible by 3 only,
     "buzz" if `number` is divisible by 5 only, the number itself if `number` is divisible by neither 3 or 5
    """

    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


for i in range(1, 101):
    print(fizz_buzz(i))
