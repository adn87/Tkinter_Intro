from tkinter import *


def button_clicked():
    print("I've been clicked")
    my_label.config(text="New Text")


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
Input = Entry(width=10)
print(Input.get())
Input.grid(column=3, row=2)

# New_Button
new_Button = Button(text="New Button", command=button_clicked)
new_Button.grid(column=2, row=0)





window.mainloop()
