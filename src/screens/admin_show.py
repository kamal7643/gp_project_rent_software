from src.screens import clear
from src import button
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
start_index = 0
start_index_c = 0
start_index_b = 0

def admin_show(root, head):
    print("admin show")
    clear.clear(root)
    # 1. gain show by cars
    # 2. all cars
    # 3. customers
    gain_button = tk.Button(root, text="Gain ", width="12", bg="purple1", font=("Arial", 10), 
    command=lambda: gain(root, head))
    cars_button = tk.Button(root, text="Cars ", width="12", bg="purple1", font=("Arial", 10), 
    command=lambda: manage_cars(root, head))
    customers_button = tk.Button(root, text="Customers ", width="12", bg="purple1", font=("Arial", 10), 
    command=lambda: manage_customers(root, head))
    gain_button.place(relx=0.35, rely=0.01)
    cars_button.place(relx=0.475, rely=0.01)
    customers_button.place(relx=0.6, rely=0.01)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "admin"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)

def gain(root, head):
    frame = tk.Frame(root, width="1000", height="500", bg="white")
    frame.place(relx=0.05, rely=0.1)
    listbox = []
    global start_index_b
    for i in range(len(head.all_cars)):
        listbox.insert(i,[head.all_cars[i].id,head.all_cars[i].model, head.all_cars[i].AC, head.all_cars[i].gain, head.all_cars[i].available])
    listbox.sort(reverse=True,key=com)
    render_list(frame,listbox,start_index_b)
    next_button = tk.Button(frame, text="next", width="12", background="gray80", font=("Arial Bold", 10),
        command=lambda: next_render_list_b(listbox,frame))
    last_button = tk.Button(frame, text="last", width="12", background="gray80", font=("Arial Bold", 10),
        command=lambda: last_render_list_b(listbox,frame))
    last_button.place(relx=0.2, rely=0.9)
    next_button.place(relx=0.75, rely=0.9)

def next_render_list_b(listbox,frame):
    global start_index_b
    if start_index_b +10 <len(listbox):
        start_index_b += 10
        render_list(frame,listbox,start_index_b)

def last_render_list_b(listbox, frame):
    global start_index_b
    if start_index_b - 10 >=0:
        start_index_b -= 10
        render_list(frame,listbox,start_index_b)

def manage_cars(root, head):
    frame = tk.Frame(root, width="1000", height="500", bg="white")
    frame.place(relx=0.05, rely=0.1)
    listbox = []
    global start_index
    for i in range(len(head.all_cars)):
        listbox.insert(i,[head.all_cars[i].id,head.all_cars[i].model, head.all_cars[i].AC, head.all_cars[i].gain, head.all_cars[i].available])
    render_list(frame,listbox,start_index)
    next_button = tk.Button(frame, text="next", width="12", background="gray80", font=("Arial Bold", 10),
        command=lambda: next_render_list(listbox,frame))
    last_button = tk.Button(frame, text="last", width="12", background="gray80", font=("Arial Bold", 10),
        command=lambda: last_render_list(listbox,frame))
    last_button.place(relx=0.2, rely=0.9)
    next_button.place(relx=0.75, rely=0.9)

def next_render_list(listbox,frame):
    global start_index
    if start_index + 10 < len(listbox):
        start_index += 10
        render_list(frame,listbox,start_index)

def last_render_list(listbox,frame):
    global start_index
    if start_index - 10 >=0:
        start_index -= 10
        render_list(frame,listbox,start_index)
    
def render_list(frame, listbox, start_index):
    lb = tk.Label(frame, text="ID", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=0*0.20, rely=0)
    lb = tk.Label(frame, text="Model", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=1*0.20, rely=0)
    lb = tk.Label(frame, text="AC", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=2*0.20, rely=0)
    lb = tk.Label(frame, text="Gain", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=3*0.20, rely=0)
    lb = tk.Label(frame, text="Available", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=4*0.20, rely=0)
    for i in range(start_index, start_index+10):
        p = i
        while p >=10:
            p -= 10
        for j in range(len(listbox[0])):
            if i < len(listbox):
                lb = tk.Label(frame, text=listbox[i][j], bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)
            else:
                lb = tk.Label(frame, bg="white", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)

def manage_customers(root, head):
    frame = tk.Frame(root, width="1000", height="500",bg="white")
    frame.place(relx=0.05, rely=0.1)
    listbox = []
    for i in range(len(head.customers)):
        listbox.insert(i,[head.customers[i].id,head.customers[i].name,head.customers[i].phone_number,head.customers[i].email,head.customers[i].car_rented_id])
    global start_index_c
    render_list_c(frame,listbox,start_index_c)
    next_button = tk.Button(frame, text="next", width="12", background="gray80", font=("Arial Bold", 10),
        command=lambda: next_render_list_c(listbox,frame))
    last_button = tk.Button(frame, text="last", width="12", background="gray80", font=("Arial Bold", 10),
        command=lambda: last_render_list_c(listbox,frame))
    last_button.place(relx=0.2, rely=0.9)
    next_button.place(relx=0.75, rely=0.9)

def next_render_list_c(listbox, frame):
    global start_index_c
    if start_index_c + 10 < len(listbox):
        start_index_c += 10
        render_list_c(frame,listbox,start_index_c)

def last_render_list_c(listbox,frame):
    global start_index_c
    if start_index_c - 10 >= 0:
        start_index_c -= 10
        render_list_c(frame,listbox, start_index_c)

def render_list_c(frame, listbox, start_index_c):
    lb = tk.Label(frame, text="ID", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=0*0.20, rely=0)
    lb = tk.Label(frame, text="Name", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=1*0.20, rely=0)
    lb = tk.Label(frame, text="Ph. No.", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=2*0.20, rely=0)
    lb = tk.Label(frame, text="Email", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=3*0.20, rely=0)
    lb = tk.Label(frame, text="Car Id", bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=4*0.20, rely=0)
    for i in range(start_index_c, start_index_c+10):
        p = i
        while p >=10:
            p -= 10
        for j in range(len(listbox[0])):
            if i < len(listbox):
                if listbox[i][j]== -1:
                    listbox[i][j] = "Na"
                listbox[i][j] = str(listbox[i][j])
                listbox[i][j] = listbox[i][j].replace("@gmail.com","")
                lb = tk.Label(frame, text=listbox[i][j], bg="seagreen", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)
            else:
                lb = tk.Label(frame, bg="white", width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)

def com(e):
    return e[3]