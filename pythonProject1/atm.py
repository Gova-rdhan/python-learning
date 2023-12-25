print("WELCOME TO THE ATM CHOSE WHATEVER YOU WANT")
amount = 5000
username = 'govi'
password = 'govi@123'

name = input('enter your name')
pas = str(input('enter your password'))
if username == name and password == pas:
    print('1 to withdraw \n 2 to deposit \n 3 to mini statement \n 4 to exit')
    option = int(input('enter your option'))
    if option ==1:
        withdraw = int(input('enter the amount'))
        if(amount-withdraw)>0:
           amount = amount - withdraw
           print('withdraw successfull')
           print(amount)
        else:
            print('insuficient balance')
    elif option ==2:
        dep = int(input('enter money to dep: '))
        amount = amount + dep
        print('toal amount is: '+str(amount))
    elif option ==3:
        print('total amount is: '+str(amount))
    elif option ==4:
        exit()
else:
    print('incorrect details')
