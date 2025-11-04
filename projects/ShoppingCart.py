# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy (q to quit): ")
    if food == "q" or food == "Q":
        break
    else:
        price = float(input(f"Enter the price of a food {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n---------Your Shopping Cart--------")
for food in foods:
    print(food, end =" ")

for  price in prices:
    total += price
print(f"\nYour total is : {total}")