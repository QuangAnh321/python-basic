computer_parts = ["computer", "monitor", "keyboard", "mouse", "Speaker"]

for part in computer_parts:
    print(part)

print()
print(computer_parts[3])

print(computer_parts[0:3])
print(computer_parts[-1])

computer_parts[3:] = ["headphone"]
print(computer_parts)

del computer_parts[0:2]
print(computer_parts)