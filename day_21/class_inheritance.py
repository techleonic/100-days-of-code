
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, Exhale")
class Fish(Animal) :
    def __init__(self):
        super().__init__()
    def swim(self):
        print("swimming")
    def breathe(self):
        print("your breathing underwater")
        super().breathe()

#when a class is inheritance of another class
#you can access both of de fuctions
nemo = Fish()
nemo.swim()
nemo.breathe()