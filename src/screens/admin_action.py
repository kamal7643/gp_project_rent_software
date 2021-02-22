from src.screens.clear import *
from src.screens.admin import *
from src.classes.vehical import *
from tkinter import messagebox
from src import do_exit


def admin_action(root, head):
    print("admin action")
    clear(root)
    change_name_label = tk.Label(text="change name :-     ",
                                 width="15",
                                 font=("Arial Bold", 10))
    change_name_label.place(relx=0.0, rely=0.05)
    change_name_entry = tk.Entry(width="20", font=("Arial bold", 12))
    change_name_entry.place(relx=0.10, rely=0.05)
    change_button = tk.Button(text="change",
                              font=("Arial Bold", 10),
                              width="10",
                              bg="gray60",
                              command=lambda: change_name(change_name_entry, root, head))
    change_button.place(relx=0.91, rely=0.05)
    handle_add_vehicle(head)
    handle_remove_vehicle(head)
    back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10))
    back_button.place(relx=0.0, rely=0.9)
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), command=lambda: do_exit.do_exit(root, head))
    exit_button.place(relx=0.91, rely=0.9)
    home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: start(root, head))
    home_button.place(relx=0.45, rely=0.9)


def change_name(entry, root, head):
    if entry.get() != "":
        if messagebox.askquestion("Access Required", "Are you sure?") == "yes":
            head.name = entry.get()
            entry.delete(0, tk.END)
            root.title(head.name)
        else:
            print("Action Cancel!")
    else:
        messagebox.showinfo("Invalid Input", "Name can't be empty string")


def handle_add_vehicle(head):
    label1 = tk.Label(text="ADD Vehicle:- ", width="12", font=("Arial Bold", 10))
    label2 = tk.Label(text="model name:", width="12", bg="gray80", font=("Arial Bold", 10))
    label3 = tk.Label(text="prize :", width="12", bg="gray80", font=("Arial Bold", 10))
    label4 = tk.Label(text="AC(yes/no):", width="12", bg="gray80", font=("Arial Bold", 10))
    label5 = tk.Label(text="per hour:", width="12", bg="gray80", font=("Arial Bold", 10))
    label6 = tk.Label(text="per K.M.:", width="12", bg="gray80", font=("Arial Bold", 10))
    label1.place(relx=0.00, rely=0.15)
    label2.place(relx=0.10, rely=0.15)
    label3.place(relx=0.25, rely=0.15)
    label4.place(relx=0.40, rely=0.15)
    label5.place(relx=0.55, rely=0.15)
    label6.place(relx=0.70, rely=0.15)
    en1 = tk.Entry(font=("Arial Bold", 12), width="8")
    en1.place(relx=0.19, rely=0.15)
    en2 = tk.Entry(font=("Arial Bold", 12), width="8")
    en2.place(relx=0.34, rely=0.15)
    en3 = tk.Entry(font=("Arial Bold", 12), width="8")
    en3.place(relx=0.49, rely=0.15)
    en4 = tk.Entry(font=("Arial Bold", 12), width="8")
    en4.place(relx=0.64, rely=0.15)
    en5 = tk.Entry(font=("Arial Bold", 12), width="8")
    en5.place(relx=0.79, rely=0.15)
    add_button = tk.Button(text="add",
                           font=("Arial bold", 10),
                           bg="gray60",
                           width="10",
                           command=lambda: add(head, en1, en2, en3, en4, en5))
    add_button.place(relx=0.91, rely=0.15)


def add(head, en1, en2, en3, en4, en5):
    if en1.get() != "":
        if en2.get() != "":
            if en3.get() != "":
                if en4.get() != "":
                    if en5.get() != "":
                        a = en2.get()
                        if a.isdigit():
                            part = en4.get()
                            partition = part.partition('.')
                            if (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
                                part = en5.get()
                                partition = part.partition('.')
                                if (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
                                    if en3.get() == "yes" or en3.get() == "no":
                                        if len(en1.get()) <= 2:
                                            messagebox.showinfo("Error", "model name should contains more than 2 char")
                                        else:
                                            if messagebox.askquestion("Access Required", "Are You Sure to Add vehicle ?") == "yes":
                                                final_add(head, en1, en2, en3, en4, en5)
                                            else:
                                                print("Action Canceled!")
                                                messagebox.showinfo("Action", "Action Canceled !")
                                    else:
                                        messagebox.showinfo("Error", "Enter yes if vehicle has AC else no")
                                else:
                                    messagebox.showinfo("Error", "per K.M. rate should be integer")
                            else:
                                messagebox.showerror("Error", "per hour should be float")
                        else:
                            messagebox.showerror("Error", "prize should be integer")
                    else:
                        messagebox.showinfo("Empty Input", "Enter float rate per K.M.")
                else:
                    messagebox.showinfo("Empty Input", "Enter float rate per hour")
            else:
                messagebox.showinfo("Empty Input", "Enter yes if vehicle has AC or no")
        else:
            messagebox.showinfo("Empty Input", "Enter prize of vehicle (integer)")
    else:
        messagebox.showinfo("Empty Input", "Enter model name for vehicle")


def final_add(head, en1, en2, en3, en4, en5):
    pid = head.all_cars[len(head.all_cars)-1].id + 1
    temp = vehical(pid)
    temp.model = en1.get()
    temp.prize = int(en2.get())
    temp.AC = en3.get()
    temp.per_hour = float(en4.get())
    temp.per_km = float(en5.get())
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
    if temp in head.all_cars:
        messagebox.showerror("Error", "Vehicle already exists!")
    else:
        head.all_cars.append(temp)
        head.availabel_cars.append(temp)
        print("added"+str(len(head.all_cars)))
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        en3.delete(0, tk.END)
        en4.delete(0, tk.END)
        en5.delete(0, tk.END)


def handle_remove_vehicle(head):
    print("not yet")