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


# for i in range(1, 101):
#     print(fizz_buzz(i))


# Pseudocode
# Player and computer take turns, game end when user guess wrong or the number to guess reached 100

# Computer start first, and from 1
# => Computer print result for odd number
# => Player print result for even number
# if player is wrong / reached 100 => break

for i in range(1, 101):
    if i % 2 == 0:
        player_answer = input(f"The number is {i}, please enter your answer: ")
        correct_answer = fizz_buzz(i)

        if player_answer == correct_answer:
            print("Correct!")
            print("Computer turn next!")
        else:
            print("Ops! Wrong answer. Game Over")
            break
    else:
        print(f"The number is {i}, the computer answer is: {fizz_buzz(i)}")
        print("Your turn next!")
