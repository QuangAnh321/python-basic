data = [4, 5, 50, 104, 105, 110, 250, 300, 500]

# del data[0:2]
# print(data)

min_valid = 100
max_valid = 200

# Unsafe way of removing item from a list
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)

# Safe way

# Process low values
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# Process high value
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # The index of the first item  (start index)
        # to delete is + 1 after the first smaller than max item
        # So we need to + 1 here
        start = index + 1
        break

print(start)
del data[start:]
print(data)

