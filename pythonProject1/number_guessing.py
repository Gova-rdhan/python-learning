import random
num = random.randint(1,100)
def game_check():
    count = 0
    level = input("choose the level you want type 'easy' for easy  and type 'hard' for hard: ")
    if level == 'easy':
        count = 10
    elif level == 'hard':
        count = 5
    endup = True
    while endup:
        guess = int(input("enter make a guess: "))
        if guess == num:
            print("you got it!!! you won the game")
            if input("if you want to continue still type y or n: ") == 'y':
               game_check()
            else:
                endup = False
        elif guess > num:
            count = count-1
            print(f"too high you have {count} more chances")
        elif guess < num:
            count = count - 1
            print(f"too low you have {count} more chances")
        if count == 0:
            print("you lost it :)")
            endup = False

game_check()




