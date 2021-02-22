from src.screens.start import *
from src.screens.return_frame import *
from src.screens.get_rent import *
from src.screens.clear import *
from src import do_exit
import tkinter as tk


def customer(root, head):
    print("customer")
    clear(root)
    rent_button = tk.Button(text="rent", width="20", background="blue", font=("Arial Bold", 12),
                            command=lambda: get_rent(root, head))
    return_button = tk.Button(text="return", width="20", background="blue", font=("Arial Bold", 12),
                              command=lambda: return_frame(root, head))
    rent_button.place(relx=0.35, rely=0.35)
    return_button.place(relx=0.35, rely=0.45)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: start(root, head))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: start(root, head))
    home_button.place(relx=0.45, rely=0.9)