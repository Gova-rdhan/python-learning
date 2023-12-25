def primecheck(n):
    # n = int(input("eneter the number: "))
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count <= 2:
        print("prime")
    else:
        print("non prime")

def checkprime(n):
    is_prime = True
    for i in range(2,n):
        if n%i == 0:
            is_prime = False
    if is_prime:
        print("prime")
    else:
        print("non prime")

checkprime(17)