import pandas as pd
import tkinter as tk

def get_rent(root):
    print("list")
    data=pd.read_excel(r'C:\Users\kamal swami\PycharmProjects\pythonProject\cache\yesorno.xlsx')
    data=pd.DataFrame(data,columns=['model','nonAC','AC'])
    print(data)
