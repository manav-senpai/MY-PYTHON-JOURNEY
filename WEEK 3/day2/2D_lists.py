# 2 dimensional lists = a list of lists

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
meats = ["chicken", "beef", "pork"]

dinner_menu = [fruits, vegetables, meats]
# print(dinner_menu)
# print(len(dinner_menu))
# print(dinner_menu[0])
# print(dinner_menu[1][2])
# print(dinner_menu[2][3]) #This will cause an index error because there is no index 3 in the meats list
for collection in dinner_menu:
    print(collection)

#2d tuples

# fruits = ("apple", "banana", "cherry")
# vegetables = ("carrot", "broccoli", "spinach")
# meats = ("chicken", "beef", "pork")
# dinner_menu = (fruits, vegetables, meats)
# print(dinner_menu)

#2d sets

# fruits = {"apple", "banana", "cherry"}
# vegetables = {"carrot", "broccoli", "spinach"}
# meats = {"chicken", "beef", "pork"}
# dinner_menu = {fruits, vegetables, meats} # this will cause an error because
# sets are unhashable and cannot be added to another set
dinner_menu = [fruits, vegetables, meats] # using a list instead
print(dinner_menu)