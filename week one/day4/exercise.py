#if the item in the list is number and  is greater than 6, then print the item;

list1 = ("munna", "babli", 5,6,8,9,76,"bittu", "moongoose")

for item in list1:
    if isinstance(item, int) and item >= 6:
        print(item) 