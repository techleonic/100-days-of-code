import  pandas

#dataframework to dictionary
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}
# print(nato_dict)

word = input("Enter a Word: ").upper()
list_letter = [nato_dict[letter] for letter in word]
print(list_letter)