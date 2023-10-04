import random 
from words import words 
import string 

def get_valid_words(words): 
    # choose a random word from the word list
    word = random.choice(words)

    # handle edge cases - choose another word
    while '-' in word or ' ' in word: 
        word = random.choice(words)

    return

def hangman(): 
    word = get_valid_words()
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # get the user's input 
    while len(word_letters) > 0:
        # print the letters used so far
        print("These letters have been guessed: "',' ''.join(used_letters))

        # what the current word is: 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ', ' '".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in used_letters: 
                word_letters.remove(user_letter)

        elif user_letter in used_letters: 
            print("You've already used that character! Try again...\n")
        else: 
            print("Invalid character. Try again...")

hangman()


