import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['~','@','#','$',"%",'^','&','*','(',')']

let = int(input("enter the no of letters: "))
num = int(input("enter no of numbers: "))
sym = int(input("enter no of symbols: "))
if(let+num+sym < 7):
    print("password must be greater than 7 cahracters")
    exit()
elif(sym <= 2):
    print("password conatins atleast 3 symbols")
    exit()
elif(num <= 2):
    print("password contains atleast  3 nums")
    exit()
elif(let <= 2):
    print("password conatins atleast 3 letters")
    exit()
le = ''
for l in range(0,let):
    le = le+letters[random.randint(0,25)]
no = ''
for n in range(0,num):
    no = no+numbers[random.randint(0,9)]
sy = ''
for s in range(0,sym):
    sy = sy+symbols[random.randint(0,9)]

password = ''.join(random.sample(le+no+sy, len(le+no+sy)))
print(password)

