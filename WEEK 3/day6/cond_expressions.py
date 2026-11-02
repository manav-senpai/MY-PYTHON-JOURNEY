num = 5

# print("positive" if num> 0 else "Negative")

result = "Even" if num%2==0 else "Odd"
print(result)

a = 6
b = 7

max_num = a if a > b else b

print(max_num)

age = input("What is your age?")
age = int(age)
status = "Adult" if age >= 18 else "child"

print(status)