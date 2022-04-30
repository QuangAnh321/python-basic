pangram = "The quick brown fox jumps over the lazy dog"
numbers = [1, 7, 2, 5, 6]
persons = ["John", "Tim", "annie", "ben", "jane"]

letters = sorted(pangram)
print(letters)

# Create a new list with sorted elements
print(sorted(numbers))

# Sort the existing list
numbers.sort()
print(numbers)

# Sort case insensitive
case_insensitive_names = sorted(persons, key=str.casefold)
print(case_insensitive_names)

# Sort case sensitive
case_sensitive_names = sorted(persons)
print(case_sensitive_names)