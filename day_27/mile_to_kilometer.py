
from tkinter import *

def button_clicked():
    miles= int(my_input.get())
    kilometer = miles*1.6
    nlabel.config(text=kilometer)

window = Tk()
window.title("mile to kilometes converter")
# window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_input = Entry(width=7)
my_input.grid(column=1, row=0)

my_label = Label(text= "miles")
my_label.grid(column=2, row=0)

my_label2 = Label(text="is equal to")
my_label2.grid(column=0,row=1)

nlabel = Label(text="0");
nlabel.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button= Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()