import random
data = [
    {
        "name": "v.kohli",
        "count": 30,
        "game": "crickter",
        "country": "Indian"
    },
    {
        "name": "m.s.dhoni",
        "count": 25,
        "game": "crickter",
        "country": "Indian"
    },
   {
        "name": "surya",
        "count": 20,
        "game": "crickter",
        "country": "Indian"
    },
    {
        "name": "gill",
        "count": 21,
        "game": "crickter",
        "country": "Indian"
    },
{
        "name": "sara",
        "count": 22,
        "game": "social media influencer",
        "country": "Indian"
    },
{
        "name": "virushka",
        "count": 29,
        "game": "Actress",
        "country": "Indian"
    },
{
        "name": "a.arjun",
        "count": 25,
        "game": "Actor",
        "country": "Indian"
    },
{
        "name": "mbabu",
        "count": 23,
        "game": "Actor",
        "country": "Indian"
    },
{
        "name": "nani",
        "count": 24,
        "game": "Actor",
        "country": "Indian"
    },
{
        "name": "ronaldo",
        "count": 31,
        "game": "Footballer",
        "country": "Portugal"
    },
{
        "name": "messi",
        "count": 32,
        "game": "footballer",
        "country": "France"
    },
{
        "name": "n.modiji",
        "count": 50,
        "game": "polotician",
        "country": "Indian"
    },
{
        "name": "ktr",
        "count": 19,
        "game": "politician",
        "country": "Indian"
    },
{
        "name": "kcr",
        "count": 18,
        "game": "politician",
        "country": "Indian"
    },
{
        "name": "annamali",
        "count": 15,
        "game": "politician",
        "country": "Indian"
    },
{
        "name": "mthakur",
        "count": 28,
        "game": "actress",
        "country": "Indian"
    }
]

def questions():
    opA = random.choice(data)
    opB = random.choice(data)
    if opA['count'] == opB['count']:
        opB = random.choice(data)
    print(f"A {opA['name']} is {opA['game']} from {opA['country']}")
    print("*****************VS**********************************")
    print(f"B {opB['name']} is {opB['game']} from {opB['country']}")
    if opA['count'] > opB['count']:
        return "A"
    elif opB['count'] > opA['count']:
        return "B"
    else:
        return "C"

def gamez():
    game = True
    score = 0
    count = 5
    while game:
        answer = questions()
        guess = input("choose A or B: ").upper()
        if guess == answer:
            score+=1
            print(f"you're right your score is {score}")
            if score == 10:
              print("congratulation you won the game")
              game = False
        else:
            count -=1
            print(f"you're wrong still you have {count} chances and your score is {score}")
            if count == 0:
                print(f"you lost and your score is {score}")
                print("===========")
                con = input("type 'y' to continue type 'n' to quit the game")
                if con == 'y':
                    gamez()
                elif con == 'n':
                    game = False





gamez()
