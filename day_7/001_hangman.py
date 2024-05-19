word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

choice = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


progres= []
for i in choice:
    progres.append("-")
print(progres)
print(choice)

word_leight =  len(choice)
players_live = 6
while "-" in progres: #keeps aksing the user to guess while still have blanks
    if players_live > 0:
        gues_letter = input("Guess letter: ").lower()
        #if letter is in the word choose replace de character in the progress list
        if gues_letter in choice:
            for i in range(word_leight):
                letter = choice[i]
                if gues_letter == letter:
                    progres[i] =  letter
        else:  #else means that the user did not choose the correct word so we take on life a draw de hangman
            print(stages[players_live-1]) 
            players_live-=1 
        print(progres)
    else: #else means that the user used all his lifes so he loses
        print("You lose")
        break #we break when the user uses all the life
if players_live != 0:
    print("You Win")