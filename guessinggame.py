answer = 5

print("Please guess a number between 1 and 10")

guess = int(input())

# if guess < answer:
#     print("Please guess higher")
# elif guess > answer:
#     print("Please guess lower")
# else:
#     print("Correct!")

if guess < answer:
    print("Please guess higher")
    print("Second chance, please try again")
    guess = int(input())
    if guess == answer:
        print("You got it right")
    else:
        print("Better luck next time")
elif guess > answer:
    print("Please guess lower")
    print("Second chance, please try again")
    guess = int(input())
    if guess == answer:
        print("You got it right")
    else:
        print("Better luck next time")
else:
    print("Correct!")