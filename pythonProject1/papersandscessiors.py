import random
user_wins = int(0)
computer_win = int(0)
options = ["rock","paper","scessiors"]
while True:
    u_choice = input("enter the choice").lower()
    if u_choice == 'q':
        break
    if u_choice not in options:
        continue
    rand = random.randint(0,2)
    computer_wins = options[rand]
    if u_choice == 'rock' and computer_wins == 'paper':
        print("you win")
        user_wins+=1
    elif u_choice == 'paper' and computer_wins == 'scessiors':
        print("you win")
        user_wins+=1
    elif u_choice == 'scessiors' and computer_wins == 'rock':
        print("you win")
        user_wins+=1
    else:
        print("computer wins")
        computer_win+=1