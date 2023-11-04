from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New Text")


def button_clicked():
    print("I've been clicked")
    my_label.config(text=Input.get())


# Button
button = Button(text="click me", command=button_clicked)
button.pack()

# Entry
Input = Entry(width=10)
Input.pack()
Input.get()




window.mainloop()
