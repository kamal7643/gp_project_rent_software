from src.screens import clear
from src import button
import tkinter as tk


def admin(root, head):
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