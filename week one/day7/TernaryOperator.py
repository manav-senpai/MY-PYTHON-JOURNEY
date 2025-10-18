#CONTITIONAL EXPRESSION = a one line shortcut for the if-else statement ( ternary operator )
#                           print or assign one of two valuse based on condition
#                           X if condition else Y



num1 = 6
a = 6
b = 7
age = 13
temperature = 27
user_role = "admin"
# print("The music's on 50 % volume...kinda creating irritation in my ears.. but just listening to it... cause of that music effect don't know what it's called.. but it's awesome")
# print("Damn.... this nahimic audio app is incredible on pc.. i want in my other devices too.. for it turns my little average headphones in good ones.. fucking awesome")

# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
#min_num = a if a < b else b

# print(f"Maximum number {max_num}")
status = "Adult" if age >= 18 else "Child"

weather = "Hot" if temperature >= 25 else "Cold"
access_level = "FULL ACCESS" if user_role == "admin" else "LIMITED ACCESS"
print(status)
print(weather)
print(access_level)

