list1 = [1, 1, 1, 1, 1]
list2 = [1, "abc", True, "abc", 1]
list3 = [99, 100]

l1 = list1.copy()
l1.reverse()
print(f"list 1 = {list1}, and reversed {l1}")

l2 = list2.copy()
l2.reverse()
print(f"list 2 = {list2}, and reversed {l2}")

l3 = list3.copy()
l3.reverse()
print(f"list 3 = {list3}, and reversed {l3}")

if( list1 == l1):
    print("list 1 is palindorme")
else:
    print("Not a palindrome")

if ( list2 == l2):
    print("list 2 is palindrome")

if ( list3 == l3):
    print("palindrome")
else:
    print("not a palindrome")