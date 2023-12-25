# enc = input("type 'encode' to encrypt,type 'decode' to decrypt").lower()
# letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# n = input("enter your message")
# shift = int(input("enter the shift number for encode"))

def encryption(shift,n):
    encrypted = ''
    for i in n:
        index = letters.index(i)
        encrypted+=letters[index+int(shift)]
    print(encrypted)

def decryption(shift,n):
    decrypted = ''
    for j in n:
        index = letters.index(j)
        position = index - shift
        decrypted += letters[position]
    print(decrypted)

should_we_con = True
while should_we_con:
    enc = input("type 'encode' to encrypt,type 'decode' to decrypt").lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    n = input("enter your message")
    shift = int(input("enter the shift number for encode"))
    def decryption_encryptions(shift, n):
        decrypted = ''
        crypted = ''
        for j in n:
            index = letters.index(j)
            if enc == 'encrypt':
                index = letters.index(j)
                crypted += letters[index + shift]
                print(crypted)
            elif enc == 'decrypt':
                position = index - shift
                crypted += letters[position]
    result = input("should we continue type yes else type no")
    if result == 'no':
        should_we_con = False
        print("good bye")



# if enc == 'encrypt':
#     encryption(shift,n)
# elif enc == 'decrypt':
#     decryption(shift,n)

decryption_encryptions(shift,n)