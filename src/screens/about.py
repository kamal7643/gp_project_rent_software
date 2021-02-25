from src.screens.clear import *
from src.screens import start
from src import do_exit
import tkinter as tk


def about(root, head):
    clear(root)
    print("about")
    label = tk.Label(text="Girish Kumar      \nKamal Swami    \nAbhishek Thakur\n"
                     + head.name+"\n"
                     + "Contact at:    "+head.help_line_number
                     + "\nowner: "+head.owner_name
                     + "\npress esc to exit app", font=("Arial Bold", 10))
    label.place(relx=0.0, rely=0.01)
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
