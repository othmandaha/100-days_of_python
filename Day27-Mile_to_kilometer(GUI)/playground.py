from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=1, column=1)

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=2,column=2)

button_2 = Button(text="click Me")
button_2.grid(row=1, column=3)

#Entries
entry = Entry(width=10)
#Add some text to begin with
#Gets text in entry
print(entry.get())
entry.grid(row=3, column=4)

window.mainloop()