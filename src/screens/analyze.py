from tkinter import messagebox
from src import button
from src.screens import clear
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg, NavigationToolbar2Tk
from PIL import ImageTk, Image


# analyze function for admin
def analyze(root, head):
    clear.clear(root)

    # frame to show graphs
    frame = tk.Frame(root, width="450", height="400", bg="cadetblue", borderwidth=3, relief=tk.GROOVE)
    frame.place(relx=0.3, rely=0.1)
    
    # list of button on header
    bts = []
    
    # earn
    earn_button = tk.Button(frame, text="earn ", width="20", bg="purple1", font=("Arial", 12), borderwidth=3, relief=tk.GROOVE,
                            command=lambda: change_frame(frame, head, "earn", bts))
    bts.append(earn_button)

    # demand
    demand_button = tk.Button(frame, text="demand ", width="20", bg="purple1", font=("Arial", 12), borderwidth=3, relief=tk.GROOVE,
                              command=lambda: change_frame(frame, head, "demand", bts))
    bts.append(demand_button)

    # spent
    spent_button = tk.Button(frame, text="spent ", width="20", bg="purple1", font=("Arial", 12), borderwidth=3, relief=tk.GROOVE,
                             command=lambda: change_frame(frame, head, "spent", bts))
    bts.append(spent_button)

    # price of cars
    price_button = tk.Button(frame, text="price ", width="20", bg="purple1", font=("Arial", 12), borderwidth=3, relief=tk.GROOVE,
                             command=lambda: change_frame(frame, head, "price", bts))
    bts.append(price_button)

    # place header buttons
    earn_button.place(relx=0.3,rely=0.15)
    demand_button.place(relx=0.3,rely=0.30)
    spent_button.place(relx=0.3,rely=0.45)
    price_button.place(relx=0.3,rely=0.60)

   
    

    # footer actions
    # back to admin home page
    back_button = tk.Button(root, text="back", width="12", background="gray80", font=("Arial", 10),
                            command=lambda: button.button(root, head, "admin"))
    back_button.place(relx=0.0, rely=0.9)
    # exit application
    exit_button = tk.Button(root, text="exit", width="12", background="gray80", font=("Arial", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    # go to landing page of the application
    home_button = tk.Button(root, text="home", width="12", background="gray80", font=("Arial", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)


# change frame
def change_frame(frame, head, txt, bts):
    if txt == "earn":
        bts[0].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[2].config(bg="gray40")
        bts[3].config(bg="gray40")
        earn(frame, head)
    elif txt == "demand":
        bts[1].config(bg="purple1")
        bts[0].config(bg="gray40")
        bts[2].config(bg="gray40")
        bts[3].config(bg="gray40")
        demand(frame, head)
    elif txt == "spent":
        bts[2].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[0].config(bg="gray40")
        bts[3].config(bg="gray40")
        spent(frame, head)
    elif txt == "price":
        bts[3].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[2].config(bg="gray40")
        bts[0].config(bg="gray40")
        price(frame, head)

def earn(frame, head):
    setcarTypes = set()
    for i in head.all_cars:
        setcarTypes.add(i.model)
    carlist = list(setcarTypes)
    
    ac_cars_gain=[]
    non_ac_cars_gain = []
    for j in range(len(carlist)):
        acprofit = 0
        nonacprofit = 0
        
        for i in head.all_cars:
            if carlist[j] == i.model :
                if i.AC =='yes':
                    acprofit = acprofit + i.gain
                else:
                    nonacprofit += i.gain
        ac_cars_gain.append(acprofit)
        non_ac_cars_gain.append(nonacprofit)

    X_axis = np.arange(len(carlist))    
    plt.bar(X_axis - 0.2, non_ac_cars_gain, 0.4, label = 'Non-Ac') 
    plt.bar(X_axis + 0.2, ac_cars_gain, 0.4, label = 'Ac') 
    plt.xticks(X_axis, carlist) 
    plt.xlabel("Cars") 
    plt.ylabel("Gain") 
    plt.title("Gain vs Car") 
    plt.legend() 
    plt.show()
    # fig = plt.Figure(figsize=(100,100), dpi=100)
    # a = fig.add_subplot(111)
    # canvas = FigureCanvasTkAgg(plt, frame)
    # canvas.show()
    # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

    


def demand(frame, head):
    setcarTypes = set()
    for i in head.all_cars:
        setcarTypes.add(i.model)
    carlist = list(setcarTypes)
    
    ac_cars_gain=[]
    non_ac_cars_gain = []
    for j in range(len(carlist)):
        acprofit = 0
        nonacprofit = 0
        
        for i in head.all_cars:
            if carlist[j] == i.model :
                if i.AC =='yes':
                    acprofit = acprofit + i.times_rented
                else:
                    nonacprofit += i.times_rented
        ac_cars_gain.append(acprofit)
        non_ac_cars_gain.append(nonacprofit)

    X_axis = np.arange(len(carlist))    
    plt.bar(X_axis - 0.2, non_ac_cars_gain, 0.4, label = 'Non-Ac') 
    plt.bar(X_axis + 0.2, ac_cars_gain, 0.4, label = 'Ac') 
    plt.xticks(X_axis, carlist) 
    plt.xlabel("Cars") 
    plt.ylabel("Demand") 
    plt.title("Demand vs Car") 
    plt.legend() 
    plt.show()

def spent(frame, head):
    setcarTypes = set()
    for i in head.all_cars:
        setcarTypes.add(i.model)
    carlist = list(setcarTypes)
    
    ac_cars_gain=[]
    non_ac_cars_gain = []
    for j in range(len(carlist)):
        acprofit = 0
        nonacprofit = 0
        
        for i in head.all_cars:
            if carlist[j] == i.model :
                if i.AC =='yes':
                    acprofit = acprofit + i.pay_for_repair
                else:
                    nonacprofit += i.pay_for_repair
        ac_cars_gain.append(acprofit)
        non_ac_cars_gain.append(nonacprofit)

    X_axis = np.arange(len(carlist))    
    plt.bar(X_axis - 0.2, non_ac_cars_gain, 0.4, label = 'Non-Ac') 
    plt.bar(X_axis + 0.2, ac_cars_gain, 0.4, label = 'Ac') 
    plt.xticks(X_axis, carlist) 
    plt.xlabel("Cars") 
    plt.ylabel("Spent") 
    plt.title("Spent vs Car") 
    plt.legend() 
    plt.show()

def price(frame, head):
    setcarTypes = set()
    for i in head.all_cars:
        setcarTypes.add(i.model)
    carlist = list(setcarTypes)
    
    ac_cars_gain=[]
    non_ac_cars_gain = []
    for j in range(len(carlist)):
        acprofit = 0
        nonacprofit = 0
        
        for i in head.all_cars:
            if carlist[j] == i.model :
                if i.AC =='yes':
                    acprofit = i.prize
                else:
                    nonacprofit = i.prize
        ac_cars_gain.append(acprofit)
        non_ac_cars_gain.append(nonacprofit)

    X_axis = np.arange(len(carlist))    
    plt.bar(X_axis - 0.2, non_ac_cars_gain, 0.4, label = 'Non-Ac') 
    plt.bar(X_axis + 0.2, ac_cars_gain, 0.4, label = 'Ac') 
    plt.xticks(X_axis, carlist) 
    plt.xlabel("Cars") 
    plt.ylabel("Price") 
    plt.title("Price vs Car") 
    plt.legend() 
    plt.show()

# end of the file
