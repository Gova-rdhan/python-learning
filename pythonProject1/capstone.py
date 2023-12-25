import random
user = []
ucount = 0
ccount = 0
com = []
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
com = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
enoufhg = True
while enoufhg:
    for i in user:
        ucount+=i
    for j in com:
        ccount+=j
    if ucount >= 21:
        print("user loose")
        enoufhg = False
        quit()
    elif ccount >= 21:
        print("computer loose")
        enoufhg = False
        quit()
    add = input(f"your choice is {user} and computer choice is {com} if you want to paly type 'y' else 'p' to pass")
    if add == 'y':
        user.append(cards[random.randint(0,12)])
    elif add == 'p':
        com.append(cards[random.randint(0,12)])
