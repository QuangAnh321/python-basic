# guitar = "PRS Custom 24"
#
# for char in guitar:
#     print(char)

number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""
extractedNumbers = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
    else:
        extractedNumbers = extractedNumbers + char

print("Separators: {0}".format(separators))
print(f"Extracted numbers: {extractedNumbers}")


