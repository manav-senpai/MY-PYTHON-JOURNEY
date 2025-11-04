# python quiz game

questions = ("How many continents are there on Earth?",
                "What is the largest ocean on Earth?",
                "Which animal lays the largest eggs?",
             "What is the most abundant gas in the Earth's atmosphere?",
             "How many bones are there in the adult human body?")

options = (("a.seven","b.six","c.eight","d.five"),
              ("a.Atlantic Ocean","b.Indian Ocean","c.Arctic Ocean","d.Pacific Ocean"),
              ("a.Ostrich","b.Shipworm","c.Elephant","d.Shark"),
              ("a.Oxygen","b.Nitrogen","c.Carbon Dioxide","d.Hydrogen"),
              ("a.206","b.201","c.210","d.199"))

answers = ("a","d","b","b","a")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (a,b,c,d) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num].upper():
        score = score + 1
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------------")

print("         RESULTS         ")
print("----------------------------")

print("Answers: ", end="")

for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")
