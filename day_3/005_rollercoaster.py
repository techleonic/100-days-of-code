print("Welcome to the rollercoaster!")
height =  int(input("What is your height in cm"))

if height >= 120:
    print("you can ride the rollercoaster")
    bill =0
    age = int(input("What is your age : "))
    if age <= 12:
        bill = 5
        print("pay 5$")
    elif age >= 12 and age <=18:
        bill = 7
        print("pay $7")
    else:
        bill= 12
        print("pay $12")

    answer = input("whant eny photos? ")
    if answer == "yes":
        bill+=3
    
    print(f"Total bill is ${bill}")


else:
    print("you can't ride de rollercoaster")