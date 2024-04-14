from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    """Generates a secure long password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend(random.choice(letters) for _ in range(nr_letters))
    password_list.extend(random.choice(symbols) for _ in range(nr_symbols))
    password_list.extend(random.choice(numbers) for _ in range(nr_numbers))

    random.shuffle(password_list)

    #joins the element of the list into a single string
    password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(0, password)

    # copies the password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fileds empty!")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Here are your information for {website}\n"
        f"Email: {email}\nPassword: {password}\nClick 'OK' to Continue.")

    if is_ok:
        with open("data.txt", "a") as f:
            f.write(f"{website}: {email} | {password}\n")
        website_input.delete(0, END)
        pass_input.delete(0, END)
        website_input.focus()
# ---------------------------- UI SETUP ------------------------------- #

#* Window setup:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#* Importing the image:
lockImage = PhotoImage(file="logo.png")

#* setting the image canvas:
ImageCanv = Canvas(width=250, height=200)
ImageCanv.create_image(100, 100, image=lockImage) #The first two arguments are x and y axis
ImageCanv.grid(row=0, column=1, columnspan=3)


#! Lables
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_lable = Label(text='Email/User:')
email_lable.grid(row=2, column=0)

password_lable = Label(text='Password:')
password_lable.grid(row=3, column=0)


#! Enteries
# Website
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
# Email
email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "Othman@email.com")
# password
pass_input = Entry(width=22)
pass_input.grid(row=3, column=1)


#! Buttons
# Generate
Gen_button = Button(text="Generate Password", command=generate)
Gen_button.grid(row=3, column=2)
# ADD
add_button = Button(text='Add', width=39, command=save)
add_button.grid(row=4, column=1, columnspan=2)


#! Keeps the window open:
window.mainloop()