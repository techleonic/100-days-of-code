from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols)for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers)for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear():
    web_entry.delete(0,END)
    password_entry.delete(0,END)
def add():
    website= web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="fill all the data", message="website and password are required")
    else:
        is_ok =messagebox.askokcancel(title=website, message=f"this are the details entered: \nEmai:{email}\nPassword:{password}\nis it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
            clear()
    # ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#labels
website_lbl =  Label(text="Website")
website_lbl.grid(column=0,row=1)
email_lbl = Label(text="Email/Username")
email_lbl.grid(column=0, row=2)
password_lbl = Label(text="Password")
password_lbl.grid(column=0, row=3)

#entries
web_entry = Entry(width=35)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(END,"Leonidas@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#buttons
generate_btn = Button(width=21,text="Generate Password",command=generate_password)
generate_btn.grid(column=2,row=3)
add_btn =  Button(width=36,text="Add",command=add)
add_btn.grid(column=1,row=4,columnspan=2)

window.mainloop()