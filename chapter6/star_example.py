numbers = (0, 1, 2, 3, 4)


# print(numbers, sep="; ")
#
# print(*numbers, sep="; ")
# print(0, 1, 2, 3, 4, sep="; ")

def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4)
