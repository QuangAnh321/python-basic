current_choice = "-"
computer_parts = []
available_parts = ["CPU", "RAM", "GPU", "Mainboard"]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice)
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
            print("{} is already in the list, so it has been removed".format(chosen_part))
        else:
            computer_parts.append(chosen_part)
            print("Adding {}".format(chosen_part))
        print("Your list now contains: ")
        print(computer_parts)
    elif current_choice == "-1":
        print(computer_parts)
    else:
        print("Please pick an option from the list below")
        for number, part in enumerate(available_parts):
            print("{0}. {1}".format(number + 1, part))
        print("0. End")
        print("-1. print out computer part list")
    current_choice = input()
