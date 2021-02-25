from src.screens import clear
from src import do_exit
from src.screens import start
import tkinter as tk
from src.screens import customer


def get_rent(root, head):
    print("rent")
    clear.clear(root)
    # data=pd.read_excel(r'C:\Users\kamal swami\PycharmProjects\pythonProject\cache\general.xlsx') make only ./cache/
    # data=pd.DataFrame(data,columns=['model','nonAC','AC'])
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10), command = lambda: customer.customer(root, head))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: start.start(root, head))
    home_button.place(relx=0.45, rely=0.9)