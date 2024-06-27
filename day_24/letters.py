
path = "./Input/Letters/starting_letter.txt"
new_letter = ""
names_path = "./Input/Names/invited_names.txt"
new_letters_path = "./Output/ReadyToSend/example.txt"
names=[]
#get all the names
with open(names_path, mode="r") as file:
    for line in file:
        names.append(line.rstrip())

#for each name in names open de model letter and raplce [name] with each name

for name in names:
    with open(path, mode="r") as file:
        content = file.read()
        new_letter = content.replace("[name]",name)
    # new path by changing the path of  the example letter to name.txt
    new_path =  new_letters_path.replace("example", name)
    #create a new letter with the new path, file name and also with the new letter
    with open(new_path, mode="w") as file:
        file.write(new_letter)

