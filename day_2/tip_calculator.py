def  main():
    print("Welcome to the  tip calculator")
    bill =  float(input("What was the total bill? $"))
    tip_porcent = int(input("how much tip would you like to give? "))
    people = int(input("How many people to split the bill? "))

    tip = (( bill * (tip_porcent / 100)) + bill)/people

    print(f"Each person should pay : {tip:.2f}")

main()