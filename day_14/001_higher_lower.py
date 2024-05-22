from game_data import data
import art
import random
from replit import clear
print(art.logo)
def formating(comparedic):
    """returns a formating string with the conten of a dictionary"""
    name = comparedic["name"]
    description =  comparedic["description"]
    contry = comparedic["country"]
    return f"{name} a {description}, from {contry}"

def compare_followers(guess, follower_a, Followers_b):
    """Check the if the users answers are correct"""
    if follower_a > Followers_b:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_over = False
compare_a =  random.choice(data)
compare_b =  random.choice(data)

while not game_over:
    if compare_a == compare_b:
        compare_b = random.choice(data)

    if score != 0:
        print(f"You are Right Current score: {score}")

    print(formating(compare_b))
    print(art.vs)
    print(formating(compare_a))

    selection =  input("Who has more followers? Type 'A' or 'B' " ).lower()
    followera =compare_a["follower_count"]
    followerb= compare_b["follower_count"]
    if(compare_followers(selection,follower_a=followera,Followers_b=followerb)):
        clear()
        score+=1
        compare_a = compare_b
        continue
    else:
        clear()
        print(art.logo)
        print(f"Sorry, That's wrong. Final score: {score}")
        game_over = True
