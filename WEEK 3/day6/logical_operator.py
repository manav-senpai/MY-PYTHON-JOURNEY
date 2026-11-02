# temp = -4
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:(
#     print("The outdoor event is cancelled"))
# else:
#     print("The outdoor event is still scheduled")
from operator import truediv

temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <=0 and is_sunny:
    print("It's cold outside ")
    print("It is sunny")
