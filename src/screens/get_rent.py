from src.screens import clear
from src import button
import tkinter as tk


def get_rent(root, head):
    print("rent")
    clear.clear(root)
    # data=pd.read_excel(r'C:\Users\kamal swami\PycharmProjects\pythonProject\cache\general.xlsx') make only ./cache/
    # data=pd.DataFrame(data,columns=['model','nonAC','AC'])
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10), command = lambda: button.button(root, head, "customer"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)