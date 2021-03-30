import tkinter as tk


# clear a frame of a window (not to cnavas)
def clear(root):
    for widget in root.winfo_children():
        if type(widget) != tk.Canvas:
            widget.destroy()
