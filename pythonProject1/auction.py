from turtle import  clear
list = {}
bidding = False
def find_highestbidder(bidder):
    high = 0
    winner = ''
    for bid in bidder:
        amount = bidder[bid]
        if amount > high:
            high = amount
            winner = bid
    print(f"the winner is {winner} and the bid amount is {high}")

while not  bidding:
    name = input("please enter your name: ")
    rate = int(input("please enter your bid: "))
    list[name] = rate
    result = input("any bidder's? type 'yes' or 'no'").lower()
    if result == 'no':
        bidding = True
        find_highestbidder(list)
    elif result == 'yes':
        clear()



