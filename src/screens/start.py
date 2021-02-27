from src.screens import clear
from src import button
import tkinter as tk


def start(root, head):
    print("start")
    clear.clear(root)
    about_button = tk.Button(text="About", width="12", background="gray80", font=("Arial Bold", 10),
                             command=lambda: button.button(root, head, "about"))
    about_button.place(relx=0.0, rely=0.9)
    customer_button = tk.Button(text="customer", width="20", background="blue", font=("Arial Bold", 12),
                                command=lambda: button.button(root, head, "customer"))
    admin_button = tk.Button(text="Admin", width="20", background="blue", font=("Arial Bold", 12),
                             command=lambda: button.button(root, head, "admin"))
    customer_button.place(relx=0.40, rely=0.35)
    admin_button.place(relx=0.40, rely=0.45)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)