import random 

# function for the computer-based guess 
def computer_guess(num): 
    low = 1 
    high = num 
    feedback = ''

    while feedback != 'c': 
        if low != high: 
            guess = random.randint(low, high)
        else: 
            guess = low 

        feedback = input(f"I guess {guess}. Is that too high [h], too low [l], or did I get it right [c]?")
        if feedback == 'h': 
            guess = guess - 1 
        elif feedback == 'l': 
            guess = guess + 1
    
    print(f"Yay! I guessed your number {guess} correctly!")

# function for user-based guess
def user_guess(num): 
    random_number = random.randint(1,num)
    guess = 0 

    while guess != random_number: 
        guess = int(input(f'Please guess a number between 1 and {num}: '))
        if guess > random_number: 
            print("Your guess is too high! Try again...")
        elif guess < random_number: 
            print("Your guess is too low! Try again...")

    print(f"Congrats!! You guessed the right number! It was {random_number}.")

print("Welcome to Guess the Number! I'll go first...")
print("Try to think of a number between 1 and 10, and I'll try to guess the number you're thinking of!\n")
computer_guess(10)

print("Now it's your turn! Try to guess the number I'm thinking of...\n")
user_guess(10)
