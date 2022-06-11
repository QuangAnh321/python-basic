available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "speaker"
}

current_choice = None
while current_choice != 0:
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")

    else:
        if current_choice is not None:
            print(f"Ops! {current_choice} is an invalid choice, the valid choices are: ")
        else:
            print("The pick an option from the following list")
            # Less efficient due to indexing the entire dict
            # for key in available_parts:
            #     print(f"{key} for {available_parts[key]}")
        for key, value in available_parts.items():
            print(f"{key} for {available_parts[key]}")

    current_choice = input("> ")
