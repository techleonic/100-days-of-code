line1 = ["","",""]
line2 = ["","",""]
line3 = ["","",""]

map = [line1,line2,line3]

print("Hiding, your treasure! x marks the spot")
position = input("")

letter = position[0].lower().strip()
abc = ["a","b","c"]
letter_index =  abc.index(letter)
number_index = int(position[1]) -1
map[number_index][letter_index] = "x"

print(f"{line1}\n{line2}\n{line3}")