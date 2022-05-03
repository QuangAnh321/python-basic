menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Remove the "spam" from each list, then print out all lists (Method 1)

# for meal_list in menu:
#     top_index = len(meal_list) - 1
#     for index, meal in enumerate(reversed(meal_list)):
#         if meal == "spam":
#             del meal_list[top_index - index]
#     print(meal_list)


# Print out the items in each list, as long as it is not "spam" (Method 2)

# for meal_list in menu:
#     for meal in meal_list:
#         if meal != "spam":
#             print(meal)

# Like method 2, but give the same output as method 1

# for meal_list in menu:
#     temp_meal_list = []
#     for meal in meal_list:
#         if meal != "spam":
#             temp_meal_list.append(meal)
#     print(temp_meal_list)

# Another solution to method 2, using .join

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))

print("abc xyz blabla".split())