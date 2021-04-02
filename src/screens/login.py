from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox


# admin login portal
def login(root, head):
    print("admin log-in")
    clear.clear(root)
    frame = tk.Frame(root,
                     width="625",
                     height="400",
                     bg="midnightblue")
    frame.place(relx=0.2, rely=0.2)
    label = tk.Label(frame, text="Password :", width="12", font=("Arial", 12))
    label.place(relx=.2, rely=0.35)
    # pin for the admin login
    en = tk.Entry(frame, width="12", font=("Arial", 12), show="*")
    en.place(relx=0.45, rely=0.35)
    en.focus()
    # cancel login
    back_button = tk.Button(frame, text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    # login button
    next_button = tk.Button(frame, text="login", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: retquest_to_login(root, head, en))
    next_button.place(relx=0.83, rely=0.9)


def retquest_to_login(root, head, en):
    # entry box has some string
    if en.get() != "":
        # if password is correct for admin login
        if head.is_admin(en.get()):
            button.button(root, head, "admin")
        # else wrong password
        else:
            messagebox.showerror("Access denied", "Incorrect password!")
            en.delete(0, tk.END)
    # entry box is empty show error
    else:
        messagebox.showerror("Access denied", "Enter Password")
