# numpad
# will use tuple here for they're faster than list
NumPad = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ("*", 0, "#"))

for row in NumPad:
    for num in row:
        print(num, end = " ")
    print()