from tkinter import *
from playground import add

def button_clicked():
    new_text = text_box.get()
    my_label.config(text=new_text)


window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

#Label
my_label = Label(text=add(3, 5, 6, 11, 0), font=("Arial", 24, "bold"))
my_label.grid(column=0, row=1)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="New Button")
new_button.grid(column=2, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=1)


window.mainloop()
