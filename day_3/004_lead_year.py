year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not lead year")
    else:
        print("Lead year")
else:
    print("Not lead year") 