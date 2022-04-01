shopping_list = ["milk", "rice", "pasta", "coke"]

item_to_find = "abc"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is None:
    print("Item not found")
else:
    print("Item found at: {}".format(found_at))
