from src.screens import clear
from src.screens import start
from src.screens import admin
from src import do_exit
import tkinter as tk


def admin_show(root,head):
    print("admin show")
    clear.clear(root)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: admin.admin(root, head))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: start.start(root, head))
    home_button.place(relx=0.45, rely=0.9)