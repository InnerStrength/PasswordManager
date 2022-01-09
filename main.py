from tkinter import *
from tkinter import messagebox
from random import randint, shuffle
import json
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
    generated_password = []
    for i in range(10):
        generated_password.append(letters[randint(0, len(letters)-1)])
    for i in range(4):
        generated_password.append(numbers[randint(0, len(numbers)-1)])
        generated_password.append(symbols[randint(0, len(symbols)-1)])
    shuffle(generated_password)

    # ---------------- Randomizes Password ----------------#
    generated_password = ''.join(generated_password)
    password_input.delete(0, END)
    password_input.insert(0, generated_password)

    # ---------------- Copies to Clipboard ----------------#
    clipboard = Tk()
    clipboard.withdraw()
    clipboard.clipboard_clear()
    clipboard.clipboard_append(generated_password)


# -------------------------- Pop-Up Generator -------------------- #
def pop_up(popup_title, popup_text):
    popup = Toplevel(takefocus=0, padx=20, pady=10)
    popup.geometry("250x100")
    popup.resizable(width=False, height=False)
    window.eval(f'tk::PlaceWindow {popup} 300x150')
    popup.title(popup_title)
    pop = Label(popup, text=popup_text)
    pop_but = Button(popup, text="Ok", width=15, command=popup.destroy, activebackground=HOVER)
    pop_but.grid(column=2, row=2, pady=10)
    pop.grid(column=2, row=1)


# -------------------------- Save Info --------------------------- #
def add_check():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
    json_dict = {
        website: {
            "User/Email": user,
            "Password": password,
        }
    }
    if user == "" or website == "" or password == "":
        messagebox.showerror(title="Missing Info", message="Missing Information: "
                                                           "\nmake sure you have all three forms filled out")
    else:
        try:
            with open("saved_accounts.json", "r") as file:
                data = json.load(file)
                data.update(json_dict)

        except FileNotFoundError:
            data = json_dict

        with open("saved_accounts.json", "w") as file:
            json.dump(data, file, indent=4)

        password_input.delete(0, END)
        website_input.delete(0, END)
        user_input.delete(0, END)

        saved_t = "Save Success"
        saved_m = " Successful Save: \n     New Info saved to passwords file     "
        pop_up(saved_t, saved_m)


# -------------------------- Load Json Data ---------------------- #
def load_data():
    try:
        with open("saved_accounts.json") as file:
            data = json.load(file)
            website = data[website_input.get()]
    except KeyError:
        messagebox.showerror("Website Not Found", "Sorry the website was not found in your saved folders"
                                                  "\nCapitalization matters. Try upper or lowercasing the website name")
    else:
        user_input.insert(0, website["User/Email"])
        password_input.insert(0, website["Password"])


# -------------------------- Window Set-UP ----------------------- #
window = Tk()
x_Left = int(window.winfo_screenwidth()/2 - 400)
y_Top = int(window.winfo_screenheight()/2 - 250)
window.geometry("+{}+{}".format(x_Left, y_Top))
window.resizable(width=False, height=False)
window.config(padx=80, pady=30)
window.title("                                                                                "
             "                                    Password Manager")


# -------------------------- GUI Set-UP -------------------------- #
canvas = Canvas(window, width=500, height=300)
logo = PhotoImage(file="lock.gif")
canvas.create_image(190, 150, image=logo)
canvas.grid(column=2, row=1, columnspan=3)

website_label = Label(text="Website:", font=FONT, anchor="e", width=15)
website_label.grid(column=1, row=2)
website_input = Entry(width=22, takefocus=1, font=FONT)
website_input.grid(column=2, row=2, pady=PAD, ipady=PAD)
search_button = Button(text="Search", width=13, font=FONT, activebackground=HOVER, command=load_data)
search_button.grid(column=3, row=2, pady=PAD)

user_label = Label(text="E-mail/Username:", font=FONT, anchor="e", width=15)
user_label.grid(column=1, row=3)
user_input = Entry(width=41, font=FONT)
user_input.grid(column=2, row=3, columnspan=2, pady=PAD, ipady=PAD)

password_label = Label(text="Generate Pass:", font=FONT, anchor="e", width=15)
password_label.grid(column=1, row=4)
password_input = Entry(width=22, font=FONT)
password_input.grid(column=2, row=4, ipady=PAD)
generate_button = Button(text="Generate", width=13, font=FONT, command=password_generator, activebackground=HOVER)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add or Update", width=40, font=FONT, command=add_check, activebackground=HOVER)
add_button.grid(column=2, row=8, columnspan=2, pady=PAD)


window.mainloop()
