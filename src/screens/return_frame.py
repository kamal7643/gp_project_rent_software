from src.screens import clear
from src import do_exit
import tkinter as tk
from src.screens import start
from src.screens import customer


def return_frame(root, head):
    print("return")
    clear.clear(root)
    label = tk.Label(text="Enter Car ID :", font=("Arial Bold", 10))
    label.place(relx=0.2, rely=.45)
    entry = tk.Entry(font=("Arial Bold", 15))
    entry.place(relx=0.33, rely=0.45)
    entry.focus()
    return_button = tk.Button(text="return", width="12", background="gray40", font=("Arial Bold", 10))
    return_button.place(relx=.85, rely=0.45)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: customer.customer(root, head))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: start.start(root, head))
    home_button.place(relx=0.45, rely=0.9)