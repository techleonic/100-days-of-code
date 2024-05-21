import random
number = []
for i in  range(100):
    number.append(i+1)

random_pick= random.choice(number)
print(random_pick)

print("Welcome to the number guessing game ")
print("i'm thinking in a number between 1 and 100 ") 
dificulty = input("Choose dificulty 'easy' o 'hard' ")
attemps = 0
if dificulty == "hard":
    attemps = 5
else:
    attemps = 10

while attemps != 0:
    print(f"You have {attemps} attemps")
    guess = int(input("Make a guess"))
    if guess == random_pick:
        print("Your Win")
        break
    elif guess > random_pick:
        print("too high")
    else:
        print("too low")
    attemps-=1
    if attemps == 0:
        print("you lose")
        break
    