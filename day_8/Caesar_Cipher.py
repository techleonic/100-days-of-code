alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encryp(normal_text,shift_number,user_direction):
    encrypt_text =[]
    for i in normal_text:
        index_alphabet = alphabet.index(i)
        number =  + shift_number if user_direction == "encode" else - shift_number
        letter_shift = alphabet[index_alphabet+number]
        encrypt_text.append(letter_shift)
    return encrypt_text

"""def decrypt (normal_text, shift_number):
    decrypt_text=[]
    for i in normal_text:
        index_alphabet = alphabet.index(i)
        letter_shift = alphabet[index_alphabet-shift_number]
        decrypt_text.append(letter_shift)
    return decrypt_text"""


text= encryp(normal_text=text,shift_number=shift,user_direction=direction)
print("".join(text))


