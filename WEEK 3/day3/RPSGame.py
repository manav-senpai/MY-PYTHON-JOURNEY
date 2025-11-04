# Rock paper scissors game

import random

options = ("rock", "paper", "scissors")
is_playing = True

while is_playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")

    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        is_playing = False
print("Thank you for playing!")

