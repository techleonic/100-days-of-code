from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear():
    web_entry.delete(0,END)
    password_entry.delete(0,END)
def add():
    website= web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
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
generate_btn = Button(width=21,text="Generate Password")
generate_btn.grid(column=2,row=3)
add_btn =  Button(width=36,text="Add",command=add)
add_btn.grid(column=1,row=4,columnspan=2)

window.mainloop()