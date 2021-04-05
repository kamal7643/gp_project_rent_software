from src.classes.vehical import *
from tkinter import messagebox
from src import button
from src.screens import clear
import tkinter as tk


# admin home add/remove page
# change name of applicatin
# add vehicle
# remove vehicle
def admin_action(root, head):
    print("admin action")
    clear.clear(root)
    change_name_label = tk.Label(text="change name :-     ",
                                 width="15",
                                 bg="deep sky blue",
                                 font=("Arial", 12))
    change_name_label.place(relx=0.0, rely=0.05)
    change_name_entry = tk.Entry(width="20", font=("Arial", 12))
    change_name_entry.place(relx=0.15, rely=0.05)
    change_button = tk.Button(text="change",
                              font=("Arial", 12),
                              width="10",
                              bg="purple1",
                              command=lambda: change_name(change_name_entry, root, head))
    change_button.place(relx=0.9, rely=0.05)
    # add vehicle portal
    handle_add_vehicle(head, root)
    label = tk.Label(text="Remove Vehicle :",
                     bg="deep sky blue",
                     font=("Arial", 12), width="15")
    label.place(relx=0.0, rely=0.5)
    lid = tk.Label(text="ID : ", font=("Arial", 12),
                    bg="deep sky blue", width="10")
    lid.place(relx=0.15, rely=0.5)
    en = tk.Entry(width="12", font=("Arial", 12))
    en.place(relx=0.25, rely=0.5)
    # show cars availabe for remove action
    # menu
    # choose_id = tk.ComboboxCombobox
    choose_button = tk.Button(text="choose", font=("Arial", 12), width="10", bg="gray60",
                              command=lambda: handle_remove_vehicle(head, en))
    choose_button.place(relx=0.4, rely=0.5)
    # remove action
    remove = tk.Button(text="remove", font=("Arial", 12), width="10", bg="purple1",
                       command=lambda: final_remove(en, head))
    remove.place(relx=0.9, rely=0.5)

    # reapir car
    label2 = tk.Label(text="Repair Vehicle :",
                     bg="deep sky blue",
                     font=("Arial", 12), width="15")
    label2.place(relx=0.0, rely=0.65)
    lid2 = tk.Label(text="ID : ", font=("Arial", 12),
                    bg="deep sky blue", width="10")
    lid2.place(relx=0.15, rely=0.65)
    en2 = tk.Entry(width="12", font=("Arial", 12))
    en2.place(relx=0.25, rely=0.65)
    choose_button2 = tk.Button(text="choose", font=("Arial", 12), width="10", bg="gray60",
                              command=lambda: handle_repair_vehicle(head, en2))
    choose_button2.place(relx=0.4, rely=0.65)
    label3 = tk.Label(text="Repair Charge:",
                        bg="deep sky blue",
                        font=("Arial", 12),
                        width="12"
                        )
    label3.place(relx=0.55, rely=0.65)
    en3 = tk.Entry(width="12", font=("Arial", 12))
    en3.place(relx=0.67, rely=0.65)
    remove2 = tk.Button(text="vehicle repaired", font=("Arial", 12), width="15", bg="purple1",
                       command=lambda: final_repair(en2, head, en3))
    remove2.place(relx=0.85, rely=0.65)
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


# change name of the applcation
def change_name(entry, root, head):
    # validate change name string
    if entry.get() != "":
        if messagebox.askquestion("Access Required", "Are you sure?") == "yes":
            head.name = entry.get()
            entry.delete(0, tk.END)
            root.title(head.name)
            head.history.append("name changed")
            head.history_changes += 1
        else:
            print("Action Cancel!")
    else:
        messagebox.showinfo("Invalid Input", "Name can't be empty string")

# handling repair cars


def handle_repair_vehicle(head, en2):
    master = tk.Tk()
    master.title("vehicles")
    master.geometry("800x400")
    # scrollbar to secondary window
    sc = tk.Scrollbar(master)
    sc.pack(side=tk.RIGHT, fill=tk.Y)
    mylist = tk.Listbox(master, font=("Arial", 12),
                        width="100", yscrollcommand=sc)
    for i in head.on_repair_cars:
        mylist.insert(tk.END, "id :"+str(i.id)+" model :"+i.model +
                      " prize :"+str(i.prize)+" AC :"+i.AC+" gain :"+str(i.gain))
    mylist.pack(side=tk.LEFT, fill=tk.BOTH)
    sc.config(command=mylist.yview)
    select_button = tk.Button(master, text="select", font=("Arial", 12), width="10", bg="gray40", command=lambda: select_item(mylist, en2, master))
    select_button.place(relx=0.85, rely=0.9)
    master.mainloop()

def final_repair(en2, head, en3):
    d= en2.get()
    if d != "":
        if d.isdigit():
            if en3.get().isdigit():
                tem = head.get_car(int(d))
                tem.repair = "no"
                tem.available = "yes"
                tem.rent = "no"
                tem.pay_for_repair += int(en3.get())
                tem.times_repaired += 1
                head.cars_changes += 1
                for i in range(len(head.on_repair_cars)):
                    if head.on_repair_cars[i].id == tem.id:
                        head.on_repair_cars.pop(i)
                        en2.delete(0, tk.END)
                        en3.delete(0, tk.END)
                        return 
                    else:
                        print("car not found in repair list")
            else:
                messagebox.showerror("Invalid input", "Charge should be integer!")
        else:
            messagebox.showerror("Invalid input", "ID should be integer!")
    else:
        messagebox.showerror("Invalid input", "Enter Id to repair car!")

# handling add vehicle action
def handle_add_vehicle(head, root):
    frame = tk.Frame(root,
                     width="800",
                     height="200",
                     bg="deep sky blue")
    frame.place(relx=0.15,rely=0.15)
    label1 = tk.Label(root, text="ADD Vehicle:- ", width="12",
                      bg="deep sky blue",
                      font=("Arial", 12))
    label2 = tk.Label(frame,text="model name:", width="12",
                      bg="gray80", font=("Arial", 12))
    label3 = tk.Label(frame,text="prize :", width="12",
                      bg="gray80", font=("Arial", 12))
    label4 = tk.Label(frame, text="AC:", width="12",
                      bg="gray80", font=("Arial", 12))
    label5 = tk.Label(frame, text="per hour:", width="12",
                      bg="gray80", font=("Arial", 12))
    label6 = tk.Label(frame, text="per K.M.:", width="12",
                      bg="gray80", font=("Arial", 12))
    label1.place(relx=0.00, rely=0.15)
    label2.place(relx=0.25, rely=0.00)
    label3.place(relx=0.25, rely=0.15)
    label4.place(relx=0.25, rely=0.30)
    label5.place(relx=0.25, rely=0.45)
    label6.place(relx=0.25, rely=0.60)
    # entry boxes for adding new car
    en1 = tk.Entry(frame, font=("Arial", 12), width="15")
    en1.place(relx=0.5, rely=0.00)
    en2 = tk.Entry(frame, font=("Arial", 12), width="15")
    en2.place(relx=0.5, rely=0.15)
    ac_var = tk.StringVar(frame)
    ac_choices = ['yes','no']
    en3 = tk.OptionMenu(frame, ac_var, *ac_choices)
    en3.place(relx=0.5, rely=0.30)
    en4 = tk.Entry(frame, font=("Arial", 12), width="15")
    en4.place(relx=0.5, rely=0.45)
    en5 = tk.Entry(frame, font=("Arial", 12), width="15")
    en5.place(relx=0.5, rely=0.60)
    add_button = tk.Button(frame, text="add",
                           font=("Arial", 12),
                           bg="purple1",
                           width="10",
                           command=lambda: add(head, en1, en2, ac_var, en4, en5))
    add_button.place(relx=0.4, rely=0.85)


# validating add vehicle data
def add(head, en1, en2, en3, en4, en5):
    # if all entry boxes are not empty
    if en1.get() != "":
        if en2.get() != "":
            if en3.get() != "":
                if en4.get() != "":
                    if en5.get() != "":
                        # validating price
                        a = en2.get()
                        if a.isdigit():
                            # validating per hour charge
                            part = en4.get()
                            partition = part.partition('.')
                            if (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
                                #    validating per km charge
                                part = en5.get()
                                partition = part.partition('.')
                                if (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
                                    # validating ac status
                                    if en3.get() == "yes" or en3.get() == "no":
                                        # validating model name for the car
                                        if len(en1.get()) <= 3:
                                            messagebox.showinfo(
                                                "Error", "model name should contains more than 2 char")
                                        else:
                                            if messagebox.askquestion("Access Required", "Are You Sure to Add vehicle ?") == "yes":
                                                # finally add new car
                                                final_add(
                                                    head, en1, en2, en3, en4, en5)
                                            else:
                                                print("Action Canceled!")
                                                messagebox.showinfo(
                                                    "Action", "Action Canceled !")
                                    else:
                                        messagebox.showinfo(
                                            "Error", "Enter yes if vehicle has AC else no")
                                else:
                                    messagebox.showinfo(
                                        "Error", "per K.M. rate should be integer")
                            else:
                                messagebox.showerror(
                                    "Error", "per hour should be float")
                        else:
                            messagebox.showerror(
                                "Error", "prize should be integer")
                    else:
                        messagebox.showinfo(
                            "Empty Input", "Enter float rate per K.M.")
                else:
                    messagebox.showinfo(
                        "Empty Input", "Enter float rate per hour")
            else:
                messagebox.showinfo(
                    "Empty Input", "choose AC status yes or no")
        else:
            messagebox.showinfo(
                "Empty Input", "Enter prize of vehicle (integer)")
    else:
        messagebox.showinfo("Empty Input", "Enter model name for vehicle")


# adding new vehicle
def final_add(head, en1, en2, en3, en4, en5):
    # all cars are stored according to id
    # so last car will have max. id number
    # generating new id for new car
    pid = head.all_cars[len(head.all_cars)-1].id + 1
    # creating new car
    temp = vehical(pid)
    # adding car info given by admin
    temp.model = en1.get()
    temp.prize = int(en2.get())
    temp.AC = en3.get()
    temp.per_hour = float(en4.get())
    temp.per_km = float(en5.get())
    # adding some default inital informations
    temp.advance = 0
    temp.milli_meter_reading_on_rent = 0
    temp.rented_time = 0
    temp.rent = "no"
    temp.gain = 0
    temp.rented_for = 0
    temp.pay_for_repair = 0
    temp.repair = "no"
    temp.times_repaired = 0
    temp.available = "yes"
    temp.times_rented = 0
    # check for unexpected error
    if temp in head.all_cars:
        messagebox.showerror("Error", "Vehicle already exists!")
    else:
        # append new car
        head.all_cars.append(temp)
        head.cars_changes += 1
        head.history.append("new car added")
        head.history_changes += 1
        head.availabel_cars.append(temp)
        print("added"+str(len(head.all_cars)))
        # clear entry boxes
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        en4.delete(0, tk.END)
        en5.delete(0, tk.END)

# handle remove action

def select_item(mylist, en, master):
    for i in mylist.curselection():
        en.delete(0,tk.END)
        txt = ""
        for j in range(len(mylist.get(i))):
            if mylist.get(i)[j] == ':':
                k=j+1
                while mylist.get(i)[k]!=' ':
                    txt += mylist.get(i)[k]
                    k += 1
                break
        en.insert(0,txt)
        
        master.destroy()
        return


def handle_remove_vehicle(head, en):
    # show cars to remove action
    # secondary window
    master = tk.Tk()
    master.title("vehicles")
    master.geometry("800x400")
    # scrollbar to secondary window
    sc = tk.Scrollbar(master)
    sc.pack(side=tk.RIGHT, fill=tk.Y)
    mylist = tk.Listbox(master, font=("Arial", 12),
                        width="100", yscrollcommand=sc)
    for i in head.availabel_cars:
        mylist.insert(tk.END, "id :"+str(i.id)+" model :"+i.model +
                      " prize :"+str(i.prize)+" AC :"+i.AC+" gain :"+str(i.gain))
    mylist.pack(side=tk.LEFT, fill=tk.BOTH)
    sc.config(command=mylist.yview)
    select_button = tk.Button(master, text="select", font=("Arial", 12), width="10", bg="gray40", command=lambda: select_item(mylist, en, master))
    select_button.place(relx=0.85, rely=0.9)
    master.mainloop()


# final remove function
def final_remove(en, head):
    d = en.get()
    # validating car id to remove car
    if d == "":
        messagebox.showerror("ID expected", "Please enter id ")
    else:
        if d.isdigit():
            d = int(d)
            for i in range(len(head.availabel_cars)):
                # if car id match
                if d == head.availabel_cars[i].id:
                    if messagebox.askquestion("Access Required", "Are you sure to remove") == 'yes':
                        head.availabel_cars.pop(i)
                        for j in range(len(head.all_cars)):
                            if d == head.all_cars[j].id:
                                del head.all_cars[j]
                                head.cars_changes += 1
                                en.delete(0, tk.END)
                                head.history.append("car removed")
                                head.history_changes += 1
                                print("removed ID :" + str(d))
                                return
        else:
            messagebox.showerror("ID expected", "ID should be integer")
