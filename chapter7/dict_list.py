available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "speaker"
}

computer_parts = {}

current_choice = None
while current_choice != 0:
    if current_choice in available_parts:
        if current_choice in computer_parts:
            # Other option
            # computer_parts.pop(current_choice)
            print(f"{computer_parts[current_choice]} is already in the list, so it will be removed")
            del computer_parts[current_choice]
        else:
            computer_parts[current_choice] = available_parts[current_choice]
            print(f"Added {computer_parts[current_choice]}")
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        # Less efficient due to indexing the entire dict
        # for key in available_parts:
        #     print(f"{key} for {available_parts[key]}")
        for key, value in available_parts.items():
            print(f"{key} for {available_parts[key]}")

    current_choice = input("> ")
