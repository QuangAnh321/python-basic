import random

answer = random.randint(1, 10)
print(answer)

while True:
    print("Please guess a number between 1 and 10")
    guess = int(input())
    if guess == 0:
        print("Game over, better luck next time!")
        break
    elif guess > answer:
        print("try guessing lower")
    elif guess < answer:
        print("try guessing higher")
    else:
        print("Correct!")
        break
