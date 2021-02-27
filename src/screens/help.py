import tkinter as tk
from src.screens import clear
from src.screens import start
from src import do_exit


def help(root, head):
    clear.clear(root)
    label = tk.Label(text="shortcut keys:-\n1. ese to exit \n 2. ctrl+m to go to home\n3. ctrl+h to help\n4. ctrl+u to customer page\n5. ctrl+d to admin page", justify=tk.LEFT)
    label.place(relx=0, rely=0)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: start.start(root, head))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)