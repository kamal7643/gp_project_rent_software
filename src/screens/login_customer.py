from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox


def login_customer(root, head):
    print("start")
    clear.clear(root)
    frame = tk.Frame(root,
                     width="625",
                     height="400",
                     bg="midnightblue")
    frame.place(relx=0.2, rely=0.2)
    label0 = tk.Label(frame, text="Username :", width="12", font=("Arial", 12))
    label0.place(relx=0.2, rely=0.22)
    label = tk.Label(frame, text="Password :", width="12", font=("Arial", 12))
    label.place(relx=.2, rely=0.35)
    en0 = tk.Entry(frame, width="20", font=("Arial", 12))
    en0.place(relx=0.45, rely=0.22)
    en = tk.Entry(frame, width="20", font=("Arial", 12), show="*")
    en.place(relx=0.45, rely=0.35)
    en0.focus()
    back_button = tk.Button(frame, text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    next_button = tk.Button(frame, text="login", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: retquest_to_login(root, head, en0, en))
    next_button.place(relx=0.83, rely=0.9)
    signup_button = tk.Button(frame, text="Sign up", width="12", background="gray80", font=("Arial Bold", 10),
                              command=lambda: button.button(root, head, "new_customer"))
    signup_button.place(relx=0.83, rely=0)


def retquest_to_login(root, head, en0, en):
    if en0.get() != "" and en.get() != "":
        if head.is_customer(en0.get(),en.get()):
            button.button(root, head, "customer")
        else:
            messagebox.showerror("Access denied", "Incorrect Username or password!")
            en.delete(0, tk.END)
            en0.delete(0, tk.END)
    else:
        messagebox.showerror("Access denied", "Enter Username and Password")
