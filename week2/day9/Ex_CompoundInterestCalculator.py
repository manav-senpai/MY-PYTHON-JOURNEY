# python compound interest calculator
from functools import total_ordering

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle can't be less than or equal to zero !! ")
    else:
        break

while True:
    rate = float(input("Enter the Interest rate amount: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero !! ")
    else:
        break

while True:
    time = float(input("Enter the Time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero !! ")
    else:
        break


# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("principle can't be less than or equal to zero !! ")
#
# while rate <= 0:
#     rate = float(input("Enter the Interest rate amount: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero !! ")
#
# while time <= 0:
#     time = float(input("Enter the Time in years: "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero !! ")

print(f"your principle amount is {principle}")
print(f"The rate of interest is {rate}")
print(f"The time in years is {time}")

total = principle * pow((1 + rate / 100),time)

print(f"Balance after {time} year/s : ${total:.2f}")