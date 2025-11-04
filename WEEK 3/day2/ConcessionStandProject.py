# concession stand program

menu = {"pizza": 10.0, "burger": 8.0, "fries": 4.0, "soda": 2.0, "salad": 6.0, "hotdog": 5.0, "ice cream": 3.0}

cart = []
total = 0
print("------------menu-------------")
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")

print("----------------------------")

while True:
    food = input("What food do you like? (q to quit): ")
    if food.lower() == "q":
        break