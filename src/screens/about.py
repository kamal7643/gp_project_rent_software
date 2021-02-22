

def about(root):
    clear(root)
    label = tk.Label(text="Girish Kumar   \nKamal Swami   \nAbhishek Thakur", font=("Arial Bold", 10))
    label.place(relx=0.0, rely=0.2)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)
