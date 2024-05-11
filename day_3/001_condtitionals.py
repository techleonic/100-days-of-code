print("Welcome to the rollercoaster!")
height =  int(input("What is your height in cm"))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age : "))
    if age <= 12:
        print("pay 12$")
    elif age >= 12 and age <=18:
        print("pay $7")
    else:
        print("pay $18")
else:
    print("you can't ride de rollercoaster")