import pandas as pd
from src.clear import *
import tkinter as tk

def get_rent(root):
    print("rent")
    clear(root)
    # data=pd.read_excel(r'C:\Users\kamal swami\PycharmProjects\pythonProject\cache\general.xlsx')
    # data=pd.DataFrame(data,columns=['model','nonAC','AC'])
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=quit)
    exit_button.place(relx=0.91, rely=0.9)