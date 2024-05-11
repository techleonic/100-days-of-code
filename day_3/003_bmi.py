height = input("Height: ")
weight = input("Weight: ")

height =  float(height)
weight = int(weight)

bmi =  weight/(height**2)

print(int(bmi))

if bmi <= 18.5:
    print(f"Your BMi is {bmi}, you are underwight")
elif bmi <= 25:
    print(f"Your BMi is {bmi}, you are normal weight")
elif bmi <= 30:
    print(f"Your BMi is {bmi}, you are slightly overweight")
elif bmi <= 35:
    print(f"Your BMi is {bmi}, you are Obese")
else:
    print(f"Your BMi is {bmi}, you are clinically obese")