import random
import string
from words import words

def get_valid_words(words):

    # choose a random word from the word list
    word = random.choice(words)

    # handle edge cases - choose another word
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman(): 
    lives = 6 

    word = get_valid_words(words)
    word_letters = set(word) # letters in the chosen word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what the user has guessed

    # get the user's input 
    while len(word_letters) > 0 and lives != 0:
        # print the letters used so far
        print("You have",lives,"guesses left. These letters have been guessed: ", " ".join(used_letters))

        # what the current word is: 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)

            if user_letter in word_letters: 
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1 
                print("Nope! That letter wasn't in the word. Try again...\n")

        elif user_letter in used_letters: 
            print("You've already used that character! Try again...\n")
        else: 
            print("Invalid character. Try again...")

    # when lives = 0 or the word is completed 
    if lives == 0: 
        print("Game over! The word was "+word)
    else: 
        print("Yay! You guessed the word, "+word+"!")

hangman()


