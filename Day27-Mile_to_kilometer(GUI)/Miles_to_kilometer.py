from tkinter import *

#* Create the window
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


#* Entry
myInput = Entry(width=10)
myInput.grid(row=0, column=1)

#*Label1 for Entry 
miles_lable = Label(text="Mile", font=("Arial", 15, "bold"))
miles_lable.grid(row=0, column=2)

#*Label2
is_equal = Label(text="is equal to", font=("Arial", 15, "bold"))
is_equal.grid(row=1, column=0)

#* Result Label
result = Label(text="0", font=("Arial", 15, "bold"))
result.grid(row=1, column=1)

#* Lable Km
km_lable = Label(text="Km", font=("Arial", 15, "bold"))
km_lable.grid(row=1, column=2)

#* function for the button
def miles_to_kilometers():
    # Conversion factor
    conversion_factor = 1.60934
    # Convert miles to kilometers
    kilometers = int(myInput.get()) * conversion_factor
    result.config(text=str(int(kilometers)))
#* Button
myButton = Button(text="Calculate", command=miles_to_kilometers)
myButton.grid(row=2, column=1)
#* keep the window open
window.mainloop()