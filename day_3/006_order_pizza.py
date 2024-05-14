print("Welcome to python pizza \nselect  your pizza size")
size = input("Small pizza (s):$15 \nMedium pizza (m):$20 \nlarge pizza (l):$25 ")

bill = 0
add = 0
name = ""
if size == "s":
    bill+=15
    add += 2
    name =  "small"
elif size == "m":
    bill+=20
    add += 3
    name =  "medium"
else:
    bill+=25
    add += 3
    name =  "large"

total = 0
addings =  input(f"Add pepperoni for {name} (y or n) +{add} ")
if addings == "y":
    total +=  bill + add
else:
    total += bill

extra =  input("Add extra cheese (y or n) +$1 ")
if extra == "y":
    total+=1

print(f"\nThank you for choosing python pizza deliveies! \nyour final bill is: ${total}")