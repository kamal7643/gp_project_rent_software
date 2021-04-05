from tkinter import messagebox
from src import button
from src.screens import clear
from src.screens import clear_frame
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg, NavigationToolbar2Tk


# analyze function for admin
def analyze(root, head):
    clear.clear(root)

    # frame to show graphs
    frame = tk.Frame(root, width="1000", height="500", bg="white")
    frame.place(relx=0.05, rely=0.1)

    # list of button on header
    bts = []
    # list of x axis entry
    listx = []

    # earn
    earn_button = tk.Button(root, text="earn ", width="12", bg="purple1", font=("Arial", 10),
                            command=lambda: change_frame(frame, head, "earn", bts, listx))
    bts.append(earn_button)

    # demand
    demand_button = tk.Button(root, text="demand ", width="12", bg="purple1", font=("Arial", 10),
                              command=lambda: change_frame(frame, head, "demand", bts, listx))
    bts.append(demand_button)

    # spent
    spent_button = tk.Button(root, text="spent ", width="12", bg="purple1", font=("Arial", 10),
                             command=lambda: change_frame(frame, head, "spent", bts, listx))
    bts.append(spent_button)

    # price of cars
    price_button = tk.Button(root, text="price ", width="12", bg="purple1", font=("Arial", 10),
                             command=lambda: change_frame(frame, head, "price", bts, listx))
    bts.append(price_button)

    # place header buttons
    earn_button.place(relx=0.25,rely=0.01)
    demand_button.place(relx=0.375,rely=0.01)
    spent_button.place(relx=0.50,rely=0.01)
    price_button.place(relx=0.625,rely=0.01)

    # x axis for all plots
   
    for i in head.all_cars:
        tem = [i.model, i.AC]
        if tem not in listx:
            listx.append(tem)
    # set default
    change_frame(frame, head, "earn", bts, listx)

    # footer actions
    # back to admin home page
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial", 10),
                            command=lambda: button.button(root, head, "admin"))
    back_button.place(relx=0.0, rely=0.9)
    # exit application
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    # go to landing page of the application
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)

# change frame
def change_frame(frame, head, txt, bts, listx):
    clear_frame.clear(frame)
    print(listx)
    if txt == "earn":
        bts[0].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[2].config(bg="gray40")
        bts[3].config(bg="gray40")
        earn(frame, head, listx)
    elif txt == "demand":
        bts[1].config(bg="purple1")
        bts[0].config(bg="gray40")
        bts[2].config(bg="gray40")
        bts[3].config(bg="gray40")
        demand(frame, head, listx)
    elif txt == "spent":
        bts[2].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[0].config(bg="gray40")
        bts[3].config(bg="gray40")
        spent(frame, head, listx)
    elif txt == "price":
        bts[3].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[2].config(bg="gray40")
        bts[0].config(bg="gray40")
        price(frame, head, listx)

def earn(frame, head, listx):
    # create canvas

    listy = []
    for i in listx:
        listy.append(0)
    for i in head.all_cars:
        tem = [i.model, i.AC]
        listy[listx.index(tem)] += i.gain
    print(listy)

    labels = []
    ac = []
    non_ac = []
    for i in range(len(listx)):
        if listx[i][0] not in labels:
            labels.append(listx[i][0])
            ac.append(0)
            non_ac.append(0)
        if listx[i][1] == "yes" :
            ac.append(listy[i])
        else :
            non_ac.append(listy[i])
      
    X_axis = np.arange(len(labels))    
    plt.bar(X_axis - 0.2, non_ac, 0.4, label = 'Non-Ac') 
    plt.bar(X_axis + 0.2, ac, 0.4, label = 'Ac') 
    plt.xticks(X_axis, labels) 
    plt.xlabel("Cars") 
    plt.ylabel("Gain") 
    plt.title("Gain vs Car") 
    plt.legend() 
    plt.show()
    
    


def demand(frame, head, listx):
    listy = []
    for i in listx:
        listy.append(0)
    for i in head.all_cars:
        tem = [i.model, i.AC]
        listy[listx.index(tem)] += i.times_rented
    print(listy)

def spent(frame, head, listx):
    listy = []
    for i in listx:
        listy.append(0)
    for i in head.all_cars:
        tem = [i.model, i.AC]
        listy[listx.index(tem)] += i.pay_for_repair
    print(listy)

def price(frame, head, listx):
    listy = []
    listy.clear()
    for i in listx:
        listy.append(0)
    for i in head.all_cars:
        tem = [i.model, i.AC]
        listy[listx.index(tem)] = i.prize
    print(listy)

# end of the file
