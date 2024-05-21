from art import logo

def add(n1,n2):
    return n1+n2

def sustraction(n1, n2):
    return n1-n2

def division(n1, n2):
    return n1 / n2

def multiplication(n1 , n2):
    return n1 * n2 
operations  = {
    "+": add, # you could save functions in a dict
    "-": sustraction,
    "*":multiplication,
    "/":division
}
def calculate():
    print(logo)
    number_1 =float(input("what's the first number: "))
    op_continue = True
    while op_continue:
        operation =  input("+\n-\n*\n/\nPick an operation: ")
        number_2 = float(input("What's the next number"))
        result = 0.0
        operation_fuction = operations[operation] #calling the function in the dict with the key
        result = operation_fuction(number_1,number_2)#using the function
        print(f"{number_1} + {number_2} ={result}")
        if input(f"Type 'y' to continue calculating with {result} or 'n' for new calculation") == "y":
            number_1 = result
            continue
        else:
            op_continue= False
            calculate()

calculate()