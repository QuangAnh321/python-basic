# for i in range(1, 20):
#     print(i)
#     print("Done")

name = input("What is you name ? ")
age = int(input(f"How old are you, {name} "))
print(age)
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please pick a candidate")
# else:
#     print(f"You are not old enough to vote, come back later in {18 - age} year(s)")


if age < 18:
    print("You are not old enough to vote, come back in {0} years".format(18 - age))
elif age == 18:
    print("You are just old enough to vote")
else:
    print("You are more than old enough to vote")