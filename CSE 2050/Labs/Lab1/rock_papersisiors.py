import random

user_win = 0
comp_win = 0 

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("type ROCK/PAPER/SCISSOR or Q to quit").lower
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue

    r = random.randint(0, 2)
    # rock = 0 paper = 1 scissors = 2
    computer_pick = options[r]
    print('Computer picked', computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissors':
        print("you win")
        user_win += 1
        continue
    elif user_input == 'paper' and computer_pick == 'rock':
        print("you win")
        user_win += 1
        continue
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("you win")
        user_win += 1
        continue
    elif user_input == computer_pick:
        print('tie, try again')
    else:
        print('you lost')
        comp_win += 1

print('you won', user_win, 'games')
print('computer won', comp_win, 'games')
print('goodbye')