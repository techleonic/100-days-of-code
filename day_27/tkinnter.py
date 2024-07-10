import tkinter

window = tkinter.Tk()
window.title("")
window.minsize(width=500, height=300)

#label
ny_label =  tkinter.Label(text="i am a label", font=("Arial",24,"bold"))
ny_label.pack()

ny_label["text"] = "New Text"
ny_label.config(text="New Text")

#button
def button_clicked():
    # ny_label["text"]= "i got clicked"
    ny_label.config(text="Button got clicked")
    strinput = input.get()
    ny_label.config(text=strinput)


button = tkinter.Button(text="Click me",command=button_clicked)
button.pack()

#entry
input = tkinter.Entry(width=10)
input.pack()

window.mainloop()
