#iterables = An object / collection that can return its elements one at a time,
# allowing it to be iterated over in a loop

# lists
# numbers = [1, 2, 3, 4, 5]

# tuple
# numbers = tuple(numbers)  # Converting list to tuple
#
#
# for ank in reversed(numbers):
#     print(ank, end=" ")
# sets
fruits = {"apple", "banana", "cherry"}

#ai autocomplete, complete the code such that this fruits will form a 3 * 3 matrix
# ai autocomplete is fucking incredible this time 😭🥲
# fruit_matrix = [fruits] * 3  # Create a list containing the set of fruits three times
# for row in fruit_matrix:
#     for fruit in row:
#         print(fruit, end=" ")
#     print()

# for fruit in (fruits):
#     print(fruit)
# name = "Mundane Mann"
#
# for character in name:
#     print(character, end ="")

# dictionary

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key,value in my_dictionary.items():
    # print(key)
    # print(key,value)
    print(f"{key} : {value}")