#create a dictionary and take input frm the user and return the meaining of the word from the dictionary

word = str(input("Enter the word to search :"))

dict1 = {
    "syntax":"The way or format of writing a proper code",
    "processor": "component that carries out processes",
    "pc": "personal computer",
    "camera": "a device to capture pictures"
}

print(f"the meaning of {word} is \"{dict1[word]}\"")