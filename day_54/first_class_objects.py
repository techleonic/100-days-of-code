def add(n1, n2):
    return n1 + n2

def multy(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(fun_name, n1, n2):
    return fun_name(n1, n2)

# functions as first clas objects
result = calculate(multy,2,2)
print(result)

#nested functions
def outer_function():
    print("im outer")
    def nested_functioc():
        print("im inner")
    nested_functioc()

outer_function()

#return function from other fuction:
def return_function():
    def inner_function():
        print("i am a function")

    return inner_function
function_r = return_function()
function_r()