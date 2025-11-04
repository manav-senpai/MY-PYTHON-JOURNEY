# random = module in Python used to generate random numbers and perform random operations.

import random

# print(help(random))
low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
number = random.choice(options) # randomly selects an item from a list or tuple
# number = random.choice(cards) # randomly selects a card from the cards list

# random.shuffle(cards)
#
# print(cards)


# number = random.randint(low, high)
# number = random.randint(1,20) # generates a random integer between 1 and 20 inclusive
# number = random.random() # generates a random float between 0.0 and 1.0

print(number)