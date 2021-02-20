from src.start import *
from src.return_frame import *
from src.get_rent import *
from src.clear import *
import tkinter as tk


def customer(root,head):
    print("customer")
    clear(root)
    rent_button = tk.Button(text="rent", width="20", background="blue", font=("Arial Bold", 12),command=lambda : get_rent(root))
    return_button = tk.Button(text="return", width="20", background="blue", font=("Arial Bold", 12),command=lambda : return_frame(root))
    rent_button.place(relx=0.35, rely=0.35)
    return_button.place(relx=0.35, rely=0.45)
    back_button = tk.Button(text="back",width="12",background="gray80",font=("Arial Bold",10),command=lambda: start(root,head))
    back_button.place(relx=0.0,rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)
    start(root,head)
    #back button code