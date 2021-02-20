from src.admin_show import *
from src.admin_action import *
from src.clear import *
import tkinter as tk

def admin(root,head):
    print("admin")
    clear(root)
    action_button = tk.Button(text="ADD or Remove",width="20", background="blue", font=("Arial Bold", 12),command=lambda: admin_action(root))
    show_button = tk.Button(text="SHOW", width="20", background="blue", font=("Arial Bold", 12),command=lambda: admin_show(root,head))
    action_button.place(relx=0.35,rely=0.35)
    show_button.place(relx=0.35,rely=0.45)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)