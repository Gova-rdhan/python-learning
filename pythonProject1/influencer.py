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
score = 0
game = True
while game:
    def gamez():
        count = 5
        opA = random.choice(data)
        opB = random.choice(data)

        def questions():
            print(f"A {opA['name']} is {opA['game']} from {opA['country']}")
            print("*****************VS**********************************")
            print(f"B {opB['name']} is {opB['game']} from {opB['country']}")

        def count_check():
            if opA['count'] > opB['count']:
                return "A"
            elif opB['count'] > opA['count']:
                return "B"
        questions()
        guess = input("type A if answer is A otherwise type B for if answer is B: ").upper()
        answer = count_check()

        if guess == answer:
            global score
            score+=1
            print(f"you're right your score is {score}")
        elif guess != answer:
            count-=1
            if count == 0:
                print("you lost")
                con = input("type 'y' to continue else type 'n' to quit the game")
                if con == 'y':
                    gamez()
                elif con == 'n':
                    quit()
                else:
                    print(f"you're wrong!!! still you have {count} chances to paly")
                    gamez()
    if count == 0 :
        con = input("type 'y' to continue else type 'n' to quit the game")
        if con == 'y':
            gamez()
        elif con == 'n':
            quit()
    else:
        gamez()

gamez()