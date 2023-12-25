print('WELCOME TO THE GAME')
count = 0
answer = input('are you ready to play? ')
if(answer.lower() != 'yes'):
    quit()
else:
    print("let's play :)")
answer = input('what is gpu? ')
if(answer.lower() == 'graphics processing unit'):
    print("correct")
    count=count+1
else:
    print("not correct")
    count=count-1
answer = input('what is cpu? ')
if(answer.lower() == 'central processing unit'):
    print("correct")
    count=count+1
else:
    print("not correct")
    count=count-1
answer = input('what is psu? ')
if(answer.lower() == 'processing unit'):
    print("correct")
    count=count+1
else:
    print("not correct")
    count=count-1
answer = input('what is ram? ')
if(answer.lower() == 'random access memory'):
    print("correct")
    count=count+1
else:
    print("not correct")
    count=count-1
print("total points is: ",count)