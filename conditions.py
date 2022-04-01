age = int(input("How old are you"))

if age >= 16 and age <= 65:
    print("You are an adult")
else:
    print("You are not an adult")

if age < 16 or age > 65:
    print("You are not an adult")
else:
    print("You are an adult")