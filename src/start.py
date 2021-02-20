from src.customer import *
from src.clear import *
from src.admin import *
import tkinter as tk


def start(root,head):
    print("start")
    clear(root)
    customer_button = tk.Button(text="customer",width="20", background="blue", font=("Arial Bold", 12),command=lambda: customer(root,head))
    admin_button = tk.Button(text="Admin", width="20", background="blue", font=("Arial Bold", 12),command=lambda: admin(root,head))
    customer_button.place(relx=0.35,rely=0.35)
    admin_button.place(relx=0.35,rely=0.45)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)