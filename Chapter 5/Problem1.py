# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

Hindi_to_English = {
    "Namaste": "Hello",
    "Dhanyawad": "Thank you",
    "Kitab": "Book",
    "Vidyalaya": "School",
    "jal": "Water",
    "bhojan": "Food",
    "mitra": "Friend",
    "ghar": "House",
    "prem": "Love",
    "shanti": "Peace"
}

word = input("Enter word:")
print(Hindi_to_English[word])

