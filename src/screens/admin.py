from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox


# admin home page
def admin(root, head):
    # if admin not logged in
    if head.logged_in != "yes":
        messagebox.showerror("Access denied", "you are not logged in!")
        button.button(root, head, "login")
    # if admin already logged in
    else:
        print("admin")
        clear.clear(root)
        # admin action page
        action_button = tk.Button(text="Action", width="20", background="blue", font=(
            "Arial Bold", 12), command=lambda: button.button(root, head, "admin_action"))
        # admin show page
        show_button = tk.Button(text="Show", width="20", background="blue", font=(
            "Arial Bold", 12), command=lambda: button.button(root, head, "admin_show"))
        action_button.place(relx=0.40, rely=0.35)
        show_button.place(relx=0.40, rely=0.45)
        # back button
        back_button = tk.Button(text="back", width="12", background="gray80", font=(
            "Arial Bold", 10), command=lambda: button.button(root, head, "start"))
        back_button.place(relx=0.0, rely=0.9)
        # exit application
        exit_button = tk.Button(text="exit", width="12", background="gray80", font=(
            "Arial Bold", 10), command=lambda: button.button(root, head, "do_exit"))
        exit_button.place(relx=0.91, rely=0.9)
        # go to landing page
        home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                                command=lambda: button.button(root, head, "start"))
        home_button.place(relx=0.45, rely=0.9)
        # log out admin account
        log_out_button = tk.Button(text="Logout", width="15", font=("Arial", 10),
                                   command=lambda: logout(root, head))
        log_out_button.place(relx=0.85, rely=0.0)


# log out admin account
def logout(root, head):
    head.logged_in = "no"
    # go to landing page
    button.button(root, head, "start")
