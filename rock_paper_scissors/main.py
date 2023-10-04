import random 

def play(): 
    user = input("Make your choice! Input 'r' for rock, 'p' for paper, and 's' for scissors: \n")
    computer = random.choice(['r','p','s'])

    if user == computer: 
        return "It's a tie!"
    
    if is_win(user, computer): 
        return "You win!"
    
    return "Oh no, you lost!"
    
def is_win(player, opponent): 
    # p > r, r > s, s > p 
    if (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p'): 
        return True
    
print(play())