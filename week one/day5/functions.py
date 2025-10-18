# user defined functions..
#try except

numm = int(input("Enter the first number :"))

nummm = input("Enter the second number")

try:
    print(f"The sum is {numm + int(nummm)}")
except Exception as e:
    print(e)

print("This line is fucking important !")