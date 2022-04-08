while True:
    print("What do you want to do today?")
    print("0. quit")
    print("1. Go to bed")
    print("2. Go to work")
    print("3. Play games")
    print("4. Practice guitar")
    print("5. Hangout with friends")
    choice = int(input())

    if 1 <= choice <= 5:
        print("Your choice is: {}".format(choice))
        break
    elif choice == 0:
        print("See you later!")
        break
    else:
        print("Your choice invalid, please try again")

