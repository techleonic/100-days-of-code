
#*args is a tuple
def add(*args):
    result = 0;
    for n in args:
        result+=n
    print(result)

add(1,2,3,4,5)

#**kargs is a dict with key and value
def calculate(n, **kwarg):
    # print(type(kwarg))
    # print(kwarg)
    #
    # for key, value in kwarg.items():
    #     print(key)
    #     print(value)
    #
    # print(kwarg["add"])

    n+= kwarg["add"]
    n*= kwarg["multiply"]
    print(n)


calculate(2, add=3,multiply=5)

class Car:
    def __init__(self,**kwargs):
        #[] will give a eror if the argument dont get pass
        self.make = kwargs["make"]
        #.get will give you none if the argument dont get pass
        self.model = kwargs.get("model")


my_car = Car(make="Toyota",model="Hilux")
print(my_car.make)
print(my_car.model)
