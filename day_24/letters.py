
path = "./Input/Letters/starting_letter.txt"
new_letter = ""
names_path = "./Input/Names/invited_names.txt"
new_letters_path = "./Output/ReadyToSend/example.txt"
names=[]
with open(names_path, mode="r") as file:
    for line in file:
        names.append(line.rstrip())


for name in names:
    with open(path, mode="r") as file:
        content = file.read()
        new_letter = content.replace("[name]",name)

    new_path =  new_letters_path.replace("example", name)
    with open(new_path, mode="w") as file:
        file.write(new_letter)

