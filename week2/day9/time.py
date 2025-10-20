import time

my_time = input("Enter the time in seconds :")
my_time = int(my_time)

for x in range(my_time, 0, -1):
# for x in reversed(range(0, my_time)):
#     print(x)
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

# time.sleep(3)

print("Time's up !")