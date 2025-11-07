#Membership operators = used to test whether a value or vaiable is found in a sequence
# (string, list, tuple, set, dictionary)
# in , not in

# word = "APPLE"
#
# letter = input("Guess a letter in the secret word : ")
#
# if letter not in word:
#     print(f"There is no {letter}")
#
# else:
#     print(f"There is a {letter}")

# students = {"Spongebob", "Patrick", "Sandy", "Squidward"}
#
# student = input("Enter the name of the student :")
#
# if student in students:
#     print(f"{student} is enrolled in the class")
# else:
#     print(f"{student} is not enrolled in the class")

# grades = {"Sandy": "A",
#           "Squidward":"B",
#           "Spongebob":"C",
#           "Patrick":"D"}
#
# student = input("Enter the name of the student :")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "manavahire60@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")