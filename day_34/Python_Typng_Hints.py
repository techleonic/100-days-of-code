age : int
# age = "leo"
print(age)

def age_check(age:int)-> str:
    if age > 18:
        return "is adult"
    else:
        return "is not a adult"

# age_check("l")