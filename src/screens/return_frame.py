from src import button
import tkinter as tk
from tkinter import messagebox
import time


def return_frame(root, head):
    print("return")
    frame = tk.Frame(root,
                     width="625",
                     height="400",
                     bg="purple3")
    frame.place(relx=0.2, rely=0.2)
    text_to_show = ""
    index = head.customers[head.logged_in_customer_index].car_rented_id
    if index == -1:
        text_to_show += "No vehicle Rented Yet to you!"
    else:
        text_to_show += "Rented vehicle -\n"
        text_to_show += "Model Name :" + head.all_cars[
            head.customers[head.logged_in_customer_index].rented_car_index].model
        text_to_show += "\nAC: " + head.all_cars[head.customers[head.logged_in_customer_index].rented_car_index].AC
        text_to_show += "\nRented for :" + str(head.customers[head.logged_in_customer_index].time_car_rented) + "hours"
        text_to_show += "\nPayment :" + str(head.customers[head.logged_in_customer_index].payment)
    label = tk.Label(frame,
                     text=text_to_show,
                     width="50",
                     bg="purple3",
                     justify=tk.LEFT,
                     anchor='nw',
                     font=("Arial", 12))
    label.place(relx=0, rely=0)
    return_button = tk.Button(frame,
                              text="return",
                              width="15",
                              bg="gray60",
                              font=("Arial", 12),
                              command=lambda: return_function(frame, head, root))
    return_button.place(relx=0.7, rely=0.01)
    back_button = tk.Button(frame,
                            text="back",
                            width="15",
                            bg="gray60",
                            font=("Arial", 12),
                            command=lambda: frame.destroy())
    back_button.place(relx=0.4, rely=0.9)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "customer"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)


def return_function(frame, head, root):
    tem = head.all_cars[head.customers[head.logged_in_customer_index].rented_car_index]
    time_used = time.time()-tem.rented_time
    time_used /= 3600
    time_used = int(time_used)
    valid_charge = head.get_charge(tem, time_used, km=0, at=2)
    tem.gain += valid_charge
    tem.rented_for = 0
    tem.rented_time = 0
    valid_charge -= tem.advance
    tem.advance = 0
    head.return_vehicle(tem)
    head.free_customer(tem)
    if head.pay(valid_charge, root):
        head.customers[head.logged_in_customer_index].payment = 0
    else:
        head.customers[head.logged_in_customer_index].payment = valid_charge
        messagebox.showinfo("payment", "Your payment is still pending!")
    print("done")
    frame.destroy()
