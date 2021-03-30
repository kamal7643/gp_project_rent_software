import tkinter as tk


# loading page has just a label with loading text
def loading(root):
    print("loading")
    label = tk.Label(text="Loading...", width="30", font=("Arial Bold",20))
    label.place(relx=0.2, rely=0.4)
