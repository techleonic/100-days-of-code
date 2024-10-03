import time


#Example of decorator:  a functions that wraps around a function and give a function nre funtionalities
def decorator_function(function):
    def wrapper_function():
        #Do something before de function
        time.sleep(2)
        function()
        #Do something after the function
    return wrapper_function

@decorator_function
def say_hello():
    # time.sleep(2)
    print("hello")

def say_bye():
    print("bye")

def say_greeting():
    print("How are you?")




say_hello()