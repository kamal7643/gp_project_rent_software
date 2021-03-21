from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox

def login(root, head):
    print("start")
    clear.clear(root)
    label = tk.Label(text="Password :", width="12", font=("Arial Bold", 10))
    label.place(relx=.2, rely=0.35)
    en = tk.Entry(width="12", font=("Arial Bold", 10))
    en.place(relx=0.35, rely=0.35)
    en.focus()
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    next_button = tk.Button(text="login", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: retquest_to_login(root, head, en))
    next_button.place(relx=0.91, rely=0.9)


def retquest_to_login(root, head, en):
    if en.get() != "":
        if head.is_admin(en.get()):
            button.button(root, head, "admin")
        else:
            messagebox.showerror("Access denied", "Incorrect password!")
            en.delete(0, tk.END)
    else:
        messagebox.showerror("Access denied", "Enter Password")