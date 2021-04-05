from src.screens import clear
from src import button
import tkinter as tk


def about(root, head):
    clear.clear(root)
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
    help_button = tk.Button(text="help", width="12", borderwidth=3, relief=tk.GROOVE, background="gray80", font=(
        "Arial Bold", 10), command=lambda: button.button(root, head, "help"))
    help_button.place(relx=0.9, rely=0.0)
    setting_button = tk.Button(text="setting", width="12", borderwidth=3, relief=tk.GROOVE, background="gray80", font=(
        "Arial Bold", 10), command=lambda: button.button(root, head, "setting"))
    setting_button.place(relx=0.9, rely=0.05)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80", borderwidth=3, relief=tk.GROOVE,
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
