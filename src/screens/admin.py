from src.screens import admin_show
from src.screens import admin_action
from src.screens import clear
from src.screens import start
from src import do_exit
import tkinter as tk


def admin(root, head):
    print("admin")
    clear.clear(root)
    action_button = tk.Button(text="Action", width="20", background="blue", font=("Arial Bold", 12), command=lambda: admin_action.admin_action(root, head))
    show_button = tk.Button(text="Show", width="20", background="blue", font=("Arial Bold", 12), command=lambda: admin_show.admin_show(root, head))
    action_button.place(relx=0.35, rely=0.35)
    show_button.place(relx=0.35, rely=0.45)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: start.start(root, head))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: start.start(root, head))
    home_button.place(relx=0.45, rely=0.9)