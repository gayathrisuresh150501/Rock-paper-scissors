import random

def play():
    user = input("Enter your choice: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie'

    if is_win(user, computer):
        return 'You won!! Yaayyy!'

    return 'You lost. Better luck next time!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())