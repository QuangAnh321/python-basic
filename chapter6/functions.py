def multiply(x: float, y: float) -> float:
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome or not

    A palindrome is a string that reads the same forwards as backwards

    The function will compare two values:
     - A "reverse" of the original String with ignore case
     - The original String with ignore case

    :param string: The `string` to be checked
    :return: True if the `string` is a palindrome, false if it is not
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palindrome(string)


def fibonacci(n):
    """
    Return the `n` th Fibonacci number, for positive `n`
    :param n:
    :return:
    """
    if 0 <= n <= 1:
        return n

    result = None

    n_minus1, n_minus2 = 1, 0

    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(10):
    print(i, fibonacci(i))
