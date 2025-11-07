#List comprehension = A concise way to creat lists in Python
#                   Compact and easier to read than traditional loops
#                   [expression for value in iterable in condition]

# doubles = []
#
# for x in range (1,11):
#     doubles.append(x * 2)
#
# print(doubles)

#List=[expression for value in iterable in condition]

# doubles = [x*2 for x in range(1,11) ]
# triples = [y * 3 for y in range(1,11)]
# print(triples)
# print(doubles)

# squares = [x ** 2 for x in range(1, 11 ) ]
# print(squares)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits = [fruit.upper() for fruit in fruits ]
# print(fruits)
#
# fruit_chars = [fruit[0] for fruit in fruits ]
# print(fruit_chars)
#
# numbers = [1,-2,3,-4,5,-6,7,-8,9,-10]
# positive_nums = [num for num in numbers if num>=0]
# negative_nums = [num for num in numbers if num<=0]
# even_nums = [num for num in numbers if num %2 == 1]
# odd_nums = [num for num in numbers if num % 2 == 1]
# print(positive_nums)
# print(negative_nums)
# print(odd_nums)
# print(even_nums)

grades = [85, 42,79,98, 56, 61,30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)