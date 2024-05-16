rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

print("What do you choose? 0 for rock, 1 for Paper, 2 for Scissors")
user = int(input(""))

def print_selec(selection):
    match selection:
        case 0:
            print(rock)
        case 1:
            print(paper)
        case 2:
            print(scissors)
        case _:
            print("")

print_selec(user)

Computer= random.randint(0,2)

print("Computer choose")
print_selec(Computer)

if user == Computer:
    print("we are even")
elif user+1 == Computer or user-2 == Computer:
    print("You lose")
elif user-1 == Computer or user-2 == Computer:
    print("You win")
else:
    print("yu type a invalid number")

