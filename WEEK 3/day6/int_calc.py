principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter a principle: "))
    if principle <= 0:
        print("Principle cant be less than or equal to 0")
while rate <=0:
    rate = float(input("Enter a interest rate: "))
    if rate <= 0:
        print("interest rate cant be less than or equal to 0")

while time <=0:
    time = int(input("Enter time in years: "))
    if time <= 0:
        print("time cant be less than or equal to 0")

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years: ${total:.2f}")