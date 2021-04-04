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

    # list of buttons of frames
    bts = []
   
 
    # gain
    gain_button = tk.Button(root, text="Gain ", width="12", bg="purple1", font=("Arial", 10),
                            command=lambda: change_frame(root, head, "gain", bts))
    bts.append(gain_button)

    # cars
    cars_button = tk.Button(root, text="Cars ", width="12", bg="purple1", font=("Arial", 10),
                            command=lambda: change_frame(root, head, "cars", bts))
    bts.append(cars_button)

    # customers
    customers_button = tk.Button(root, text="Customers ", width="12", bg="purple1", font=("Arial", 10),
                                 command=lambda: change_frame(root, head, "customers", bts))
    bts.append(customers_button)
                    
     # set default frame to gain frame
    change_frame(root, head, "gain", bts)

    
    # place header buttons
    gain_button.place(relx=0.35, rely=0.01)
    cars_button.place(relx=0.475, rely=0.01)
    customers_button.place(relx=0.6, rely=0.01)

    # go back to admin home page
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "admin"))
    back_button.place(relx=0.0, rely=0.9)

    # exit application
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)

    # go to landing page of the application
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)

# gian show frame of master window

# change frame
def change_frame(root, head, txt, bts):
    if txt== "gain":
        bts[0].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[2].config(bg="gray40")
        gain(root, head, bts)
    elif txt == "cars":
        bts[1].config(bg="purple1")
        bts[0].config(bg="gray40")
        bts[2].config(bg="gray40")
        manage_cars(root, head, bts)
    else:
        bts[2].config(bg="purple1")
        bts[1].config(bg="gray40")
        bts[0].config(bg="gray40")
        manage_customers(root, head, bts)

def gain(root, head, bts):
    frame = tk.Frame(root, width="1000", height="500", bg="white")
    frame.place(relx=0.05, rely=0.1)
    # list to show
    listbox = []
    global start_index_b
    for i in range(len(head.all_cars)):
        # insert to list
        listbox.insert(i, [head.all_cars[i].id, head.all_cars[i].model,
                       head.all_cars[i].AC, head.all_cars[i].gain, head.all_cars[i].available])

    # sort list with the help of comparator function
    listbox.sort(reverse=True, key=com)

    # render list
    render_list(frame, listbox, start_index_b)

    # next items of the list
    next_button = tk.Button(frame, text="next", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: next_render_list_b(listbox, frame))

    # last items of the list
    last_button = tk.Button(frame, text="last", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: last_render_list_b(listbox, frame))
    last_button.place(relx=0.2, rely=0.9)
    next_button.place(relx=0.75, rely=0.9)


# set render range(next) to show in gain frame
def next_render_list_b(listbox, frame):
    global start_index_b
    if start_index_b + 10 < len(listbox):
        start_index_b += 10
        render_list(frame, listbox, start_index_b)

# set render range(last) to show in gain frame


def last_render_list_b(listbox, frame):
    global start_index_b
    if start_index_b - 10 >= 0:
        start_index_b -= 10
        render_list(frame, listbox, start_index_b)


# show all cars
def manage_cars(root, head, bts):
    frame = tk.Frame(root, width="1000", height="500", bg="white")
    frame.place(relx=0.05, rely=0.1)
    # list of cars
    listbox = []
    global start_index
    for i in range(len(head.all_cars)):
        # insert to list
        listbox.insert(i, [head.all_cars[i].id, head.all_cars[i].model,
                       head.all_cars[i].AC, head.all_cars[i].gain, head.all_cars[i].available])

    # render list
    render_list(frame, listbox, start_index)

    # next range of car list
    next_button = tk.Button(frame, text="next", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: next_render_list(listbox, frame))

    # last range of car list
    last_button = tk.Button(frame, text="last", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: last_render_list(listbox, frame))
    last_button.place(relx=0.2, rely=0.9)
    next_button.place(relx=0.75, rely=0.9)

# set render range(next) to show in cars frame


def next_render_list(listbox, frame):
    global start_index
    if start_index + 10 < len(listbox):
        start_index += 10
        render_list(frame, listbox, start_index)

# set render range(last) to show in cars frame


def last_render_list(listbox, frame):
    global start_index
    if start_index - 10 >= 0:
        start_index -= 10
        render_list(frame, listbox, start_index)

# render cars


def render_list(frame, listbox, start_index):
    # header for the frame
    lb = tk.Label(frame, text="ID", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=0*0.20, rely=0)
    lb = tk.Label(frame, text="Model", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=1*0.20, rely=0)
    lb = tk.Label(frame, text="AC", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=2*0.20, rely=0)
    lb = tk.Label(frame, text="Gain", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=3*0.20, rely=0)
    lb = tk.Label(frame, text="Available", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=4*0.20, rely=0)

    # body for the frame
    for i in range(start_index, start_index+10):
        p = i
        while p >= 10:
            p -= 10
        for j in range(len(listbox[0])):
            if i < len(listbox):
                lb = tk.Label(frame, text=listbox[i][j], bg="seagreen",
                              width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)
            else:
                lb = tk.Label(frame, bg="white", width="20",
                              justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)


# show customers in customers frame
def manage_customers(root, head, bts):
    frame = tk.Frame(root, width="1000", height="500", bg="white")
    frame.place(relx=0.05, rely=0.1)
    # list of customers
    listbox = []
    for i in range(len(head.customers)):
        # insert to list
        listbox.insert(i, [head.customers[i].id, head.customers[i].name,
                       head.customers[i].phone_number, head.customers[i].email, head.customers[i].car_rented_id])
    global start_index_c

    # render cusomers in frame
    render_list_c(frame, listbox, start_index_c)

    # next customers
    next_button = tk.Button(frame, text="next", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: next_render_list_c(listbox, frame))

    # last customers
    last_button = tk.Button(frame, text="last", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: last_render_list_c(listbox, frame))
    last_button.place(relx=0.2, rely=0.9)
    next_button.place(relx=0.75, rely=0.9)


# set render range(next) to show customers list in frame
def next_render_list_c(listbox, frame):
    global start_index_c
    if start_index_c + 10 < len(listbox):
        start_index_c += 10
        render_list_c(frame, listbox, start_index_c)

# set render range(last ) to show customers list in frame


def last_render_list_c(listbox, frame):
    global start_index_c
    if start_index_c - 10 >= 0:
        start_index_c -= 10
        render_list_c(frame, listbox, start_index_c)


# render customer's list in frame in master window
def render_list_c(frame, listbox, start_index_c):
    # header for frame
    lb = tk.Label(frame, text="ID", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=0*0.20, rely=0)
    lb = tk.Label(frame, text="Name", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=1*0.20, rely=0)
    lb = tk.Label(frame, text="Ph. No.", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=2*0.20, rely=0)
    lb = tk.Label(frame, text="Email", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=3*0.20, rely=0)
    lb = tk.Label(frame, text="Car Id", bg="seagreen", width="20",
                  justify=tk.LEFT, anchor='nw', font=("Arial", 12))
    lb.place(relx=4*0.20, rely=0)

    # body for frame
    for i in range(start_index_c, start_index_c+10):
        p = i
        while p >= 10:
            p -= 10
        for j in range(len(listbox[0])):
            if i < len(listbox):
                if listbox[i][j] == -1:
                    listbox[i][j] = "Na"
                listbox[i][j] = str(listbox[i][j])
                # making shor to  show to gmail id
                listbox[i][j] = listbox[i][j].replace("@gmail.com", "")
                lb = tk.Label(frame, text=listbox[i][j], bg="seagreen",
                              width="20", justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)
            else:
                lb = tk.Label(frame, bg="white", width="20",
                              justify=tk.LEFT, anchor='nw', font=("Arial", 12))
                lb.place(relx=j*0.20, rely=(p+1)*0.07)


# comparator function to sort gain list
def com(e):
    return e[3]
