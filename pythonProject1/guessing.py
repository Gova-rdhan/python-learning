import random
n = input("enter a number")
if n.isdigit():
    n = int(n)
    if n < 0:
        print("please enter the value grater than 0")
else:
    print("please enter the number")
rand = random.randint(0,n)
guess = 0
while True:
    guess += 1
    guess_num = input("make a guess ")
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print("enter a number")

    if guess_num == rand:
        print("you got it correct")
        break
    else:
        print("make a guess again")
print("you got it in ",guess,"guesses")