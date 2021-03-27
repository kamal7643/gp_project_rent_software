from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox
import time


def get_rent(root, head):
    print("rent")
    clear.clear(root)
    b_rules_button = tk.Button(text="Rules", width="20",
                               bg="green", font=("Arial Bold", 12),
                               anchor='sw',
                               command=lambda: rules(root, head))
    b_rules_button.place(relx=0.4, rely=0.3)
    get_car = tk.Button(text="Get vehicle", width="20",
                        bg="green", font=("Arial Bold", 12),
                        anchor='sw',
                        command=lambda: get_vehicle(root, head))
    get_car.place(relx=0.4, rely=0.38)
    status = tk.Button(text="Status", width="20",
                       bg="green", font=("Arial Bold", 12),
                       anchor='sw',
                       command=lambda: check_status(root, head))
    status.place(relx=0.4, rely=0.46)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "customer"))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    home_button.place(relx=0.45, rely=0.9)


def rules(root, head):
    frame = tk.Frame(root, width="625", height="400", bg="purple3")
    frame.place(relx=0.2, rely=0.2)
    label = tk.Label(frame,
                     text="Business Rules:-\n" +
                     "1. A car can be rented for a minimum 4 hours.\n" +
                     "2. Maximum of per hour charge and per km charge will be\napplied.\n" +
                     "3. An Ac vehicle of a particular category is charged 50%\nmore" +
                     "than a non-AC vehicle of the same category.\n" +
                     "4. There is a charge of RS 150 for every night halt " +
                     "regardless\nof the type of the vehicle.\n" +
                     "5. When a customer books a car, he has to deposit\nan advance amount\n",
                     width="50",
                     bg="purple3",
                     justify=tk.LEFT,
                     anchor='nw',
                     font=("Arial", 12))
    label.place(relx=0, rely=0)
    back_button = tk.Button(frame,
                            text="back",
                            width="15",
                            bg="gray60",
                            font=("Arial", 12),
                            command=lambda: frame.destroy())
    back_button.place(relx=0.4, rely=0.9)


def get_vehicle(root, head):
    if head.customers[head.logged_in_customer_index].car_rented_id != -1:
        messagebox.showinfo("Attention", "You have already vehicle")
    else:
        frame = tk.Frame(root,
                         width="625",
                         height="400",
                         bg="purple3")
        frame.place(relx=0.2, rely=0.2)
        label1 = tk.Label(frame, text="Model Name:",
                          width="10",
                          bg="gray60",
                          font=("Arial", 12))
        model_var = tk.StringVar(frame)
        model_choices = []
        for i in head.availabel_cars:
            if not(i.model in model_choices):
                model_choices.append(i.model)
        model_var.set(model_choices[0])
        label1.place(relx=0, rely=0)
        model_drop = tk.OptionMenu(frame, model_var, *model_choices)
        model_drop.place(relx=0.2, rely=0)
        label2 = tk.Label(frame, text="AC",
                          width="10",
                          bg="gray60",
                          font=("Arial", 12))
        ac_var = tk.StringVar(frame)
        ac_choices = []
        for i in head.availabel_cars:
            if not(i.AC in ac_choices):
                ac_choices.append(i.AC)
        ac_var.set(ac_choices[0])
        label2.place(relx=0, rely=0.1)
        ac_drop = tk.OptionMenu(frame, ac_var, *ac_choices)
        ac_drop.place(relx=0.2, rely=0.1)
        label3 = tk.Label(frame, text="hours",
                          width="10",
                          bg="gray60",
                          font=("Arial", 12))
        hour_var = tk.IntVar(frame)
        hour_choices = []
        for i in range(25):
            if i > 3:
                hour_choices.append(i)
        hour_var.set(hour_choices[0])
        label3.place(relx=0, rely=0.2)
        hour_drop = tk.OptionMenu(frame, hour_var, *hour_choices)
        hour_drop.place(relx=0.2, rely=0.2)
        list_av_button = tk.Button(frame,
                                   text="Available cars",
                                   bg="gray50",
                                   font=("Arial", 12),
                                   command=lambda: list_cars(root, head))
        list_av_button.place(relx=0.2, rely=0.3)
        get_now_button = tk.Button(frame,
                                   text="get now",
                                   bg="gray50",
                                   font=("Arial", 12),
                                   command=lambda: get_now(model_var, ac_var, hour_var, head, frame, root))
        get_now_button.place(relx=0.7, rely=0.3)
        back_button = tk.Button(frame,
                                text="back",
                                width="15",
                                bg="gray60",
                                font=("Arial", 12),
                                command=lambda: frame.destroy())
        back_button.place(relx=0.4, rely=0.9)


def check_status(root, head):
    frame = tk.Frame(root,
                     width="625",
                     height="400",
                     bg="purple3")
    frame.place(relx=0.2, rely=0.2)
    text_to_show = ""
    index = head.customers[head.logged_in_customer_index].car_rented_id
    if index == -1:
        text_to_show += "No vehicle Rented to you!"
    else:
        text_to_show += "Rented vehicle -\n"
        text_to_show += "Model Name :" + head.all_cars[head.customers[head.logged_in_customer_index].rented_car_index].model
        text_to_show += "\nAC: "+head.all_cars[head.customers[head.logged_in_customer_index].rented_car_index].AC
        text_to_show += "\nRented for :" + str(head.customers[head.logged_in_customer_index].time_car_rented)+"hours"
        text_to_show += "\nPayment :" + str(head.customers[head.logged_in_customer_index].payment)
    label = tk.Label(frame,
                     text=text_to_show,
                     width="50",
                     bg="purple3",
                     justify=tk.LEFT,
                     anchor='nw',
                     font=("Arial", 12))
    label.place(relx=0, rely=0)
    back_button = tk.Button(frame,
                            text="back",
                            width="15",
                            bg="gray60",
                            font=("Arial", 12),
                            command=lambda: frame.destroy())
    back_button.place(relx=0.4, rely=0.9)


def get_now(model, ac, hour, head, frame, root):
    for i in range(len(head.all_cars)):
        tem = head.all_cars[i]
        if messagebox.askquestion("Are You Sure?","Charge will be ("+str(head.get_charge(tem, hour.get(), km=0))+")")=="yes":
            if tem.model == model.get() and tem.AC == ac.get() and tem.available == "yes":
                amount = int(head.get_charge(tem, hour.get(), km=0))
                if head.pay(amount/2, root):
                    head.customers[head.logged_in_customer_index].payment += amount-amount/2
                    tem.advance = amount/2
                    tem.rented_for = hour.get()
                    head.customers[head.logged_in_customer_index].car_rented_id = tem.id
                    head.customers[head.logged_in_customer_index].rented_car_index = i
                    head.customers[head.logged_in_customer_index].rented_car_index_second = len(head.on_rent_cars)
                    head.customers[head.logged_in_customer_index].time_car_rented = hour.get()
                    head.remove_from_available(tem)
                    tem.available = "no"
                    tem.times_rented += 1
                    tem.rented_time = time.time()
                    head.add_to_on_rent(tem)
                    frame.destroy()
                    return

def list_cars(root, head):
    frame = tk.Frame(root,
                     width="625",
                     height="400",
                     bg="purple1")
    frame.place(relx=0.2, rely=0.2)
    l = []
    for i in head.availabel_cars:
        x = [str(i.model), str(i.AC), str(i.prize), str(i.gain)]
        if not(x in l):
            l.append(x)
    length = len(l)
    if length > 10:
        length *= 0
        length += 10
    y=0
    lb = tk.Label(frame, text="model                                    AC",
                  width="30", font=("Arial", 10))
    lb.place(relx=0, rely=y)
    y += 0.07
    for i in range(length):
       lb = tk.Label(frame, width="30",
                     text=l[i][0]+"                                  "+l[i][1],
                     font=("Arial", 10))
       lb.place(relx=0, rely=y)
       y += 0.07


    back_button = tk.Button(frame,
                            text="back",
                            width="15",
                            bg="gray60",
                            font=("Arial", 12),
                            command=lambda: frame.destroy())
    back_button.place(relx=0.4, rely=0.9)
