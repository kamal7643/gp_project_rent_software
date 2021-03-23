from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox


def admin(root, head):
    if head.logged_in != "yes":
        messagebox.showerror("Access denied", "you are not logged in!")
        button.button(root, head, "login")
    else:
        print("admin")
        clear.clear(root)
        action_button = tk.Button(text="Action", width="20", background="blue", font=("Arial Bold", 12), command=lambda: button.button(root, head, "admin_action"))
        show_button = tk.Button(text="Show", width="20", background="blue", font=("Arial Bold", 12), command=lambda: button.button(root, head, "admin_show"))
        action_button.place(relx=0.40, rely=0.35)
        show_button.place(relx=0.40, rely=0.45)
        back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: button.button(root, head, "start"))
        back_button.place(relx=0.0, rely=0.9)
        exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: button.button(root, head, "do_exit"))
        exit_button.place(relx=0.91, rely=0.9)
        home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                                command=lambda: button.button(root, head, "start"))
        home_button.place(relx=0.45, rely=0.9)
        log_out_button = tk.Button(text="Logout", width="15", font=("Arial", 10),
                                   command=lambda: logout(root, head))
        log_out_button.place(relx=0.85, rely=0.07)


def logout(root, head):
    head.logged_in = "no"
    button.button(root, head, "start")
