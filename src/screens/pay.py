from src import button
from src.screens import clear
import tkinter as tk


def pay(root, head, amount):
    clear.clear(root)
    v = tk.StringVar()
    v.set(amount)
    en = tk.Entry(font=("Arial Bold", 10), width="10", textvariable=v)
    en.place(relx=0.35, rely=0.35)
    pay_button = tk.Button(root, text="Pay", font=("Arial Bold", 10), width="10")
    pay_button.place(relx=0.9, rely=0.35)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)