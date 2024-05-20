

programming_dictionary = {
 "Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again."
 }

print(programming_dictionary["Bug"])#"Loop": "The action of doing something Over and over again"
programming_dictionary["Loop"] = "The action of doing something Over and over again"


#programming_dictionary = {} #wipe dictionary

#edit dict
programming_dictionary["Bug"] = "a moth in your computer"


#loop trough a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

