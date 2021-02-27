import tkinter as tk
from src import button
from src.screens import clear


def setting(root, head):
    clear.clear(root)
    sound_label = tk.Label(root, text="Sound ", font=("Arial", 10), width="10")
    sound_label.place(relx=0.0, rely=0.02)
    v = tk.StringVar()
    v.set(head.sound)
    sound_button = tk.Checkbutton(root, text="on", variable=v, onvalue="on", offvalue="off")
    sound_button.place(relx=0.15, rely=0.02)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)


def change_sound_status(root, head, f):
    button.button(root, head, f)