shopping_list = ["milk", "rice", "pasta", "coke"]

for item in shopping_list:
    if item != "milk":
        print("Buy "+item)


# Same as above and same as "continue" in Java
for item in shopping_list:
    if item == "milk":
        continue

    print("Buy "+item)