def add(first, second):
    return first + second
def mul(first, second):
    return first * second
def sub(first, second):
    return first - second
def div(first, second):
    return first / second

operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
def calculator():
    first = int(input("enter first number: "))
    for i in operations:
        print(i)
    should_continue = True
    while should_continue:
        opr = input("enter the operation: ")
        second = int(input("enter second number: "))
        operation = operations[opr]
        answer = operation(first,second)
        if input(f"type 'y' to continue with previous calc {answer} else 'n' to exit or start a new calc") == 'y':
            first = answer
        else:
            should_continue = False
            print("starting the new calculation")
            print("==============================")
            calculator()
calculator()