shopping_list = ["bread", "rice",  "vegetable"]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["eggs"]
print(shopping_list)
print(id(shopping_list))
