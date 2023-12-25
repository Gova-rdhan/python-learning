import  random
letters = ['antant','batbat','ratrat','elephant','creama','laptop','cellphone']
letter = random.choice(letters)
lives = 6
l = list(letter)
for le in range(0,len(letter)):
    l[le]='_'
print(l)
end_of_g = False
while not end_of_g:
    guess = input("guess a letter: ").lower()
    for position in range(len(letter)):
        let = letter[position]
        if let == guess:
            l[position] = let
    if guess not in letter:
        lives -=1
        print("you have remaining: ", lives)
        if lives == 0:
            print('you loose game over!!!')
            end_of_g = True
    print(l)
    if '_' not in l:
        end_of_g = True
        print("you win!!!! game over!!!!")




