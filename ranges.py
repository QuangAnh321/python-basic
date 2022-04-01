# for loop Java style
# equivalent to for(int i = 1; i < 20; i++)
for i in range(1, 20):
    print("i is now {}".format(i))

# equivalent to for(int i = 0; i < 20; i++)
for i in range(10):
    print("i is now {}".format(i))

# equivalent to for(int i = 10; i >= 0; i = i -2)
for i in range(10, 0, -2):
    print("i is now {}".format(i))