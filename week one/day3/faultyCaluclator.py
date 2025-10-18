# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4

operator = int(input("Select one operation (1-4):\n" \
"1 addition\n" \
"2 substraction\n" \
"3 multiplication\n" \
"4 division\n"))

num1 = int(input( "Enter the first number :"))
num2 = int(input("Enter the second number"))

if ( num1 == 45 and operator == 3 and num2 == 3):
    print("answer = 555")
elif( num1 == 56 and operator == 1 and num2 == 9):
    print("answer = 77")
elif(num1 == 56 and operator == 4 and num2 == 6):
    print("answer = 4")
else:
    if ( operator == 1):
        print(f"answer = { num1 + num2}")
        
    elif(operator == 2):
        print(f"answer = { num1 - num2}")

    elif(operator == 3):
        print(f"answer = { num1 * num2}")

    elif(operator == 4):
        print(f"answer = { num1 / num2}")
    else:
        print("Invalid operation !")