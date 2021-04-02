import tkinter as tk
from src.screens import clear


# loading page has just a label with loading text
def loading(root):
    print("loading")
    clear.clear(root)
    label = tk.Label(text="Loading...", width="30", font=("Arial Bold",20))
    label.place(relx=0.2, rely=0.4)
