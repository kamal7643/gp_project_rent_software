from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox


def login_customer(root, head):
    print("start")
    clear.clear(root)
    label = tk.Label(text="Password :", width="12", font=("Arial", 20))
    label.place(relx=.2, rely=0.35)
    en = tk.Entry(width="12", font=("Arial Bold", 20), show="*")
    en.place(relx=0.45, rely=0.35)
    en.focus()
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    next_button = tk.Button(text="login", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: retquest_to_login(root, head, en))
    next_button.place(relx=0.91, rely=0.9)
    signup_button = tk.Button(text="Sign up", width="12", background="gray80", font=("Arial Bold", 10),
                              command=lambda: button.button(root, head, "new_customer"))
    signup_button.place(relx=0.9, rely=0)


def retquest_to_login(root, head, en):
    if en.get() != "":
        if head.is_customer(en.get()):
            button.button(root, head, "customer")
        else:
            messagebox.showerror("Access denied", "Incorrect password!")
            en.delete(0, tk.END)
    else:
        messagebox.showerror("Access denied", "Enter Password")