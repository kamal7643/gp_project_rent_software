import tkinter as tk
from src.clear import *
# from src.RentalSoftware import *
# from src.vehical import *

def admin_show(root,head):
    print("admin show")
    clear(root)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)