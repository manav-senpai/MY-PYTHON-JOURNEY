#dictionary = a collection of {key: value} pairs
# ordered, changeable, no duplicate keys

capitals = {
    "us": "washington dc",
    "india": "new delhi",
    "germany": "berlin",
    "china": "beijing",
}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("india"))
#
# print(capitals.get("Japan")) # will return None if key not found
#
# if capitals.get("japan"):
#     print("That capital exists")
# else:
#     print("No such capital in the dictionary")

capitals.update({"japan": "tokyo"})
capitals.update({"germany": "munich"}) # will update existing key

# capitals.pop("china") # removes key value pair
# capitals.popitem() # removes last inserted key value pair

# capitals.clear() # clears the dictionary

# little tricky methods

# keys = capitals.keys()
# print(keys)
#
# for key in capitals.keys(): # it returns the keys of the dictionary
#     print(key)

# values = capitals.values() # it returns the values of the dictionary
# print(values)
for value in capitals.values():
    print(value)

items = capitals.items() # returns the key value pairs as tuples in a list
print(items)

for key, value in capitals.items():
    print(f"key : {key} >> value : {value}")