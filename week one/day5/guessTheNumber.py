# hide any number in the program, and ask user to guess the number, the program will loop until the correct guess.

number1 = 25

print("The total number of guesses 10 ")
guesnum = 9

guess = int(input("Guess the number :"))
        
while ( guess != number1 ):
    
    if (guesnum > 0):
            print(f"You're left with {guesnum} number of guesses \n")
    else:
            print("Ohh..No.. You're outta guesses ! \n")
            print("GAME OVER")
    print("fuck your brain motherfucker !")
    if (guess > number1 and guesnum == 0):
        break
    elif(guess > number1 and guesnum > 0):
        print("The entered number is bigger !")
    else:
        print("The entered number is smaller !")
    guess = int(input("Enter the correct number :"))
    guesnum = guesnum-1

if (guess == number1):
    print("Congratulations correct guess !!")