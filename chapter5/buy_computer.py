current_choice = "-"
computer_part = []

while current_choice != "0":
    if current_choice in "12345":
        if current_choice == "1":
            computer_part.append("CPU")
        elif current_choice == "2":
            computer_part.append("RAM")
        elif current_choice == "3":
            computer_part.append("GPU")
        elif current_choice == "4":
            computer_part.append("Mainboard")
        print("Adding {}".format(current_choice))
    elif current_choice == "-1":
        print(computer_part)
        print(current_choice)
    else:
        print("Please pick an option from the list below")
        print("1. CPU")
        print("2. RAM")
        print("3. GPU")
        print("4. Mainboard")
        print("0. End")
        print("-1. print out computer part list")
    current_choice = input()

