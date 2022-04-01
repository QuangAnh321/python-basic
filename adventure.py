# available_exits = ["north", "south", "east", "west"]
#
# chosen_exit = ""
# while True:
#     chosen_exit = input("Where do you want to go next? ")
#     if chosen_exit == "quit":
#         print("Game over, better luck next time!")
#         break
#     elif chosen_exit in available_exits:
#         print("You got out, congratulation!")
#         break
#     else:
#         continue


# for i in range(0, 100, 7):
#     if i % 11 == 0 and i != 0:
#         print(i)
#         print("end!")
#         break
#


# i = 1
#
# while i < 21:
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)
#         i += 1
#     else:
#         i += 1
#         continue

i = 1

while True:
    if i == 21:
        break

    if i % 3 != 0 and i % 5 != 0:
        print(i)
    i += 1