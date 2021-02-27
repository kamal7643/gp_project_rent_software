from src.screens.clear import *
from src.screens import start
from src import do_exit
from src.screens import help
import tkinter as tk


def about(root, head):
    clear(root)
    print("about")
    label = tk.Label(root, text="Girish Kumar      \nKamal Swami    \nAbhishek Thakur\n"
                     + head.name+"\n"
                     + "Contact at:    "+head.help_line_number
                     + "\nowner: "+head.owner_name
                     + "\npress esc to exit app"
                     + "\npress BackSpace to go to home",
                     justify=tk.LEFT,
                     font=("Arial Bold", 10))
    label.place(relx=0, rely=0)
    help_button = tk.Button(text="help", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: help.help(root, head))
    help_button.place(relx=0.9, rely=0.0)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda:start.start(root, head))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)
