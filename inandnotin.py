# Doc link: https://docs.python.org/3/library/stdtypes.html
randomText = "cinema abcxyz"
guessText = input("Enter random text ")

if guessText in randomText:
    print("The text you entered is in randomText")
else:
    print("The text you entered is not in randomText")

# if "abcxyz" in randomText:
#     print("The text you entered is in randomText")
# else:
#     print("The text you entered is not in randomText")
