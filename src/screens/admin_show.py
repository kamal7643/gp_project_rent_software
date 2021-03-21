from src.screens import clear
from src import button
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def admin_show(root, head):
    print("admin show")
    x_list_to_show = []
    y_list_to_show = []
    for i in head.all_cars:
        x_list_to_show.append(i.model)
        y_list_to_show.append(i.gain)
    final_show(root, head, x_list_to_show, y_list_to_show);


def final_show(root, head, x, y):
    clear.clear(root)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "admin"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", image=plt, width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)