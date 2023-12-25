menu = {
    "tea" : {
        "milk": 100,
        "water": 50,
        "powder": 20,
        "price": 40
    },
    "cofee":{
        "milk": 150,
        "powder": 30,
        "water": 50,
        "price": 100
    },
    "capchuno":{
        "milk": 200,
        "powder": 50,
        "water": 50,
        "price": 200
    }
}
t_water = 200
t_powder = 200
t_milk = 200

def menu_list():
    for i in menu:
        print("=========================")
        print(i,":")
        print("milk: ",menu[i]['milk'])
        print("water: ",menu[i]['water'])
        print("powder:",menu[i]['powder'])
        print("price: ",menu[i]['price'])
        print("=========================")
menu_list()

o_coins = 1
f_coins = 5
t_coins = 10

def pay():
    sm_coins = int(input("enter the no of one rupee coins: "))
    mm_coins = int(input("enter the no of five rupee coins: "))
    lm_coins = int(input("enter the no of ten rupee coins: "))

    return sm_coins*o_coins+mm_coins*f_coins+lm_coins*t_coins
def total_quantiy(water=1000,powder=500,milk=500):
    t_water = water
    t_powder = powder
    t_milk = milk
    return  print(f"machine have {t_water}ml water, {t_powder}ml of cofee powder and {t_milk}ml of milk")

def making(n):
    global t_milk,t_powder,t_water
    t_water = t_water - menu[n]['water']
    t_powder = t_powder - menu[n]['powder']
    t_milk = t_milk - menu[n]['milk']
def bill(amount,price):
    if amount >= price:
        return True
    else:
        return False
def check(choose):
    if t_milk > menu[choose]['milk'] and t_water > menu[choose]['water'] and t_powder > menu[choose]['powder'] :
        return True
    else:
        return False

def continue_making():
    st = input("still want to continue prees 'y' for yes or 'n' for no: ")
    if st == "y":
        return processing()
    elif st == "n":
        return exit()
def processing():
    still = True

    while still:
        choose = input("what do you want 'tea/cofee/capchuno': ").lower()
        if choose not in("tea","cofee","capchuno"):
            print("you just need to choose the above 3 only ")
            choose = input("what do you want: ").lower()
        price = menu[choose]['price']
        amount = pay()
        if bill(amount,price):
            if check(choose):
                making(choose)
                print(f"{choose} is here!! thank you take it")
                if amount >= price:
                    print(f"here is your change: {amount-price} please take it!!!")
                continue_making()
            else:
                if t_milk <= menu[choose]['milk']:
                    print(f"insuficient milk sorry for the inconvinience here is your amount {amount} !!")
                    exit()
                elif t_water <= menu[choose]['water']:
                    print(f"insuficient water sorry for the inconvinience here is your amount {amount} !!")
                elif t_powder <= menu[choose]['powder']:
                    print(f"insuficient powder sorry for the inconvinience here is your amount {amount} !!")
        else:
            print("money is not sufficiant")
            continue_making()

processing()

