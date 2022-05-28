import random

highest = 1000
answer = random.randint(1, highest)
print(answer)


def get_integer(prompt):
    """
    Get in an integer from Standard Input if it is valid

    The function will continue looping, and prompting user
    until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they are prompted to enter the value
    :return: The valid integer that the user entered
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print(f"Ops ! {temp} is not a valid number")


# guess = 0
# print("Please guess a number between 1 and 10")
#
# while guess != answer:
#     guess = get_integer(": ")
#     if guess == 0:
#         print("Game over, better luck next time!")
#         break
#     elif guess > answer:
#         print("try guessing lower")
#     elif guess < answer:
#         print("try guessing higher")
#     else:
#         print("Correct!")
#         break

print(get_integer.__doc__)
help(get_integer)
