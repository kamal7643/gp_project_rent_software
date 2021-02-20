import tkinter as tk

def return_frame(root):
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(text="Enter Car ID :",font=("Arial Bold",10))
    label.place(relx=0.2,rely=.45)
    entry = tk.Entry(font=("Arial Bold",15),)
    entry.place(relx=0.33,rely=0.45)
    entry.focus()
    return_button = tk.Button(text="return",width="12",background="gray40",font=("Arial Bold",10))
    return_button.place(relx=.85,rely=0.45)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)