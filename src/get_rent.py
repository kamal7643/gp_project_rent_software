import pandas as pd
import tkinter as tk

def get_rent(root):
    data=pd.read_excel(r'C:\Users\kamal swami\PycharmProjects\pythonProject\cache\general.xlsx')
    data=pd.DataFrame(data,columns=['model','nonAC','AC'])

    print(data)
