from PIL import ImageTk, Image
import tkinter as tk


def clear(root):
    for widget in root.winfo_children():
        if type(widget) != tk.Canvas:
            widget.destroy()
