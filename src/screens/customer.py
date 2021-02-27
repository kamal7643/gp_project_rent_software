from src.screens.clear import *
from src import button
import tkinter as tk


def customer(root, head):
    print("customer")
    clear(root)
    rent_button = tk.Button(text="rent", width="20", background="blue", font=("Arial Bold", 12),
                            command=lambda: button.button(root, head, "get_rent"))
    return_button = tk.Button(text="return", width="20", background="blue", font=("Arial Bold", 12),
                              command=lambda: button.button(root, head, "return_frame"))
    rent_button.place(relx=0.40, rely=0.35)
    return_button.place(relx=0.40, rely=0.45)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)