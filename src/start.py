from src.customer import *
import tkinter as tk


def start(root):
    for widget in root.winfo_children():
        widget.destroy()
    customer_button = tk.Button(text="customer", width="20", background="blue", font=("Arial Bold", 12),command=lambda: customer(root))
    admin_button = tk.Button(text="Admin", width="20", background="blue", font=("Arial Bold", 12))
    customer_button.place(relx=0.35,rely=0.35)
    admin_button.place(relx=0.35,rely=0.45)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)