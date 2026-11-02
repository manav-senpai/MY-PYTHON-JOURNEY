unit = input(("Is this temp in Celsius or Fahrenheit ? (C / F) :"))

temp = float ( input ("Enter the temperature : "))

if unit == "C" :
    temp = ((temp * 9) / 5 + 32)
    print(f"The temperature in fahrenheit is {round(temp, 2)}°F ")
elif unit == "F" :
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"the temperature in Celsius is : {temp} °C")
else :
    print(f"{unit} is not a valid unit")

# this is writing random comments on this pycyharm ide..jut for the sake of video