# collection = single " variable " used to store multiple values in a single location.

# list = []  # ordered, changeable, allows duplicate values
# tuple = ()  # ordered, unchangeable, allows duplicate values
# set = {}  # unordered, unchangeable*, no duplicate values
# dictionary = {key: value}  # unordered, changeable, no duplicate keys


#list
# fruits = ["apple", "orange", "banana", "cherry"]

# print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)
# print(help(fruits))
# print(dir(fruits))
# print(len(fruits))
# print("orange" in fruits)
# fruits.append("kiwi")
# fruits.remove("banana")
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)

#set

# fruits = {"apple", "orange", "banana", "cherry"}
# print(dir(fruits))
# print("pineapple" in fruits)

# printn(fruits[0])  # will cause an error because sets are unordered
# fruits.remove("orange")
# fruits.add("guava")
# fruits.pop()

# print(fruits)
# fruits.clear()
# print(fruits)

#tuple
fruits = ("apple", "orange", "banana", "coconut","cherry","cherry")
# print(dir(fruits))

# print("inject gallanium into the vein, dr cameron please process with the injection")
# print(fruits.index("apple"))
# print(fruits.count("cherry"))
# print(fruits.count("apple"))
# print(fruits)