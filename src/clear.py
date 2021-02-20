import tkinter as tk

def clear(root):
    for widget in root.winfo_children():
        widget.destroy()