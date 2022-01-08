from tkinter import *
from random import randint, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

# -------------------------- Global Variables -------------------- #
HOVER = "#80b3ff"
FONT = ("verdana", 12, 'normal')
PAD = 3


# -------------------------- Password Generator -------------------- #
def password_generator():
    global password
    password = []
    for i in range(10):
        password.append(letters[randint(0, len(letters)-1)])
    for i in range(4):
        password.append(numbers[randint(0, len(numbers)-1)])
        password.append(symbols[randint(0, len(symbols)-1)])
    shuffle(password)
    password_input.delete(0, END)
    password_input.insert(0, ''.join(password))
    print(password)


# -------------------------- Window Set-UP ----------------------- #
window = Tk()
window.minsize(width=800, height=500)
window.maxsize(width=800, height=500)
window.config(padx=80, pady=30)
window.title("Password Manager")

# -------------------------- GUI Set-UP -------------------------- #
canvas = Canvas(window, width=500, height=300)
logo = PhotoImage(file="lock.gif")
canvas.create_image(190, 150, image=logo)
canvas.grid(column=2, row=1, columnspan=3)

website_label = Label(text="Website:", font=FONT, anchor="e", width=15)
website_label.grid(column=1, row=2)
website_input = Entry(width=41, takefocus=1, font=FONT)
website_input.grid(column=2, row=2, columnspan=2, pady=PAD, ipady=PAD)

user_label = Label(text="E-mail/Username:", font=FONT, anchor="e", width=15)
user_label.grid(column=1, row=3)
user_input = Entry(width=41, font=FONT)
user_input.grid(column=2, row=3, columnspan=2, pady=PAD, ipady=PAD)

password_label = Label(text="Password:", font=FONT, anchor="e", width=15)
password_label.grid(column=1, row=4)
password_input = Entry(width=22, font=FONT)
password_input.grid(column=2, row=4, ipady=PAD)
generate_button = Button(text="Generate", width=13, font=FONT, command=password_generator)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=40, font=FONT)
add_button.grid(column=2, row=8, columnspan=2, pady=PAD)


window.mainloop()
