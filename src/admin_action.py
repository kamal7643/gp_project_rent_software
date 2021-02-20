from src.clear import *
import tkinter as tk

def admin_action(root):
    print("admin action")
    clear(root)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)