from src.classes.vehical import *
from src.classes.customer import *
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import datetime


# master class to handle software
class RentalSoftware:
    name = ""
    owner_name = ""
    owner_phone_number = ""
    help_line_number = ""
    sound = ""
    bg_file_name = ""
    logged_in = "no"
    logged_in_customer = "no"
    customer_id = -1
    logged_in_customer_index = -1
    password = ""
    all_cars = []
    on_rent_cars = []
    on_repair_cars = []
    available_cars = []
    general_data = []
    customers = []
    history = []
    history_changes = 0
    cars_changes = 0
    customers_changes = 0
    mails = []
    email_id = "TAAS.SE.LAB.01@gmail.com"
    email_password = "taasadmin"

    # init for software
    def __init__(self, name, owner_name, owner_phn, helpline, sound, bg_file_name, pin):
        self.name = name
        self.owner_name = owner_name
        self.owner_phone_number = owner_phn
        self.help_line_number = helpline
        self.sound = sound
        self.bg_file_name = bg_file_name
        self.all_cars.clear()
        self.on_rent_cars.clear()
        self.on_repair_cars.clear()
        self.available_cars.clear()
        self.password = pin

    # store all data in master class object (software)
    def __fetch__(self):

        # reading cars
        data = pd.read_excel(r'./cache/cars.xlsx')
        data = pd.DataFrame(data, columns=['id',
                                           'model',
                                           'repair',
                                           'rent',
                                           'available',
                                           'price',
                                           'times_rented',
                                           'times_repaired',
                                           'pay_for_repair',
                                           'gain',
                                           'rented_for',
                                           'rented_time',
                                           'milli_meter_reading_on_rent',
                                           'AC',
                                           'advance',
                                           'per_hour',
                                           'per_km'])

        self.available_cars.clear()
        self.all_cars.clear()
        self.on_rent_cars.clear()
        self.on_repair_cars.clear()
        for i in range(len(data)):

            # creating cars
            temp = vehical(i)
            temp.id = data['id'][i]
            temp.model = data['model'][i]
            temp.repair = data['repair'][i]
            temp.rent = data['rent'][i]
            temp.available = data['available'][i]
            temp.price = data['price'][i]
            temp.times_rented = data['times_rented'][i]
            temp.times_repaired = data['times_repaired'][i]
            temp.pay_for_repair = data['pay_for_repair'][i]
            temp.gain = data['gain'][i]
            temp.rented_for = data['rented_for'][i]
            temp.rented_time = data['rented_time'][i]
            temp.milli_meter_reading_on_rent = data['milli_meter_reading_on_rent'][i]
            temp.AC = data['AC'][i]
            temp.advance = data['advance'][i]
            temp.per_hour = data['per_hour'][i]
            temp.per_km = data['per_km'][i]
            self.all_cars.append(temp)
            if temp.repair == "yes":
                self.on_repair_cars.append(temp)
            if temp.rent == "yes":
                self.on_rent_cars.append(temp)
            if temp.available == "yes":
                self.available_cars.append(temp)

        # reading customers
        customer_data = pd.read_excel(r'./cache/customers.xlsx')
        customer_data = pd.DataFrame(customer_data, columns=['id',
                                                             'name',
                                                             'phone_number',
                                                             'email',
                                                             'licence',
                                                             'car_rented_id',
                                                             'rented_car_index',
                                                             'rented_car_index_second',
                                                             'time_rented',
                                                             'time_to_return',
                                                             'payment',
                                                             'username',
                                                             'password'])
        self.general_data.clear()
        self.customers.clear()

        # creating customers
        for i in range(len(customer_data)):
            temp = Customer(customer_data['id'][i])
            temp.profile(customer_data['name'][i],
                         customer_data['phone_number'][i],
                         customer_data['email'][i],
                         customer_data['licence'][i],
                         customer_data['car_rented_id'][i],
                         customer_data['rented_car_index'][i],
                         customer_data['rented_car_index_second'][i],
                         customer_data['time_rented'][i],
                         customer_data['time_to_return'][i],
                         customer_data['payment'][i],
                         customer_data['username'][i],
                         customer_data['password'][i])
            self.customers.append(temp)
        self.history.clear()

        # history of the software (storing)
        f = open("cache/history.txt", "r")
        line = f.readline()
        while line:
            self.history.append(line[:-1])
            line = f.readline()

    # function to handle admin login
    def is_admin(self, password):
        if self.password == password:
            self.logged_in = "yes"
            return True
        else:
            return False

    # function to handle customer login

    def is_customer(self, username, password):
        temp_index = -1
        for i in self.customers:
            temp_index += 1
            if i.username == username and i.password == password:
                self.logged_in_customer = "yes"
                self.customer_id = i.id
                self.logged_in_customer_index = temp_index
                return True

    # check if with same data already software has a customer account or not (sign up proccess)

    def is_double_customer(self, other):
        for i in self.customers:
            if i.email == other.email or i.phone_number == other.phone_number:
                return True
        return False

    # check possibility for username in customer sign up action

    def is_possible_username(self, password):
        for i in self.customers:
            if i.username == password:
                return False
        return True

    # delete customer account

    def delete_customer(self, id):
        self.customers_changes += 1
        for i in range(len(self.customers)):
            if self.customers[i].id == id:
                self.customers.pop(i)
                self.history.append("Account deleted!")
                return True
        return False

    # get car object by id
    def get_car(self, id):
        for i in self.all_cars:
            if i.id == id:
                return i

    # get customer object by id

    def get_customer(self, id):
        for i in self.customers:
            if i.id == id:
                return i
        return None

    # after rent , remove this car from available cars list

    def remove_from_available(self, tem):
        for i in range(len(self.available_cars)):
            if self.available_cars[i].model == tem.model and self.available_cars[i].AC == tem.AC:
                self.available_cars.pop(i)
                return True

    # add car to list of on rent cars

    def add_to_on_rent(self, tem):
        self.on_rent_cars.append(tem)
        return True

    # compute charge
    def get_charge(self, tem, hour, km, at):
        curr_time = datetime.datetime.now()
        if hour < 4:
            hour = 4

        # computing charge (advance)
        if at == 1:
            if tem.per_hour > tem.per_km:
                if curr_time.hour >= 18 or curr_time.hour <= 6:
                    if tem.AC == "yes":
                        return int(tem.per_hour*hour*(3/2)+150)
                    return tem.per_hour*hour+150
                return tem.per_hour*hour
            else:
                if curr_time.hour >= 3 or curr_time.hour <= 6:
                    if tem.AC == "yes":
                        return int(tem.per_km*km*(3/2)+150)
                    return tem.per_km*km+150
                return tem.per_km*km
        # compute charge (on the time of returning car)
        else:
            if tem.per_hour > tem.per_km:
                if curr_time.hour >= 18 or curr_time.hour <= 6 or hour >= 12:
                    if tem.AC == "yes":
                        return int(tem.per_hour*hour*(3/2)+150)
                    return tem.per_hour*hour + 150
                return tem.per_hour*hour
            else:
                if curr_time.hour >= 18 or curr_time.hour <= 6 or hour >= 12:
                    if tem.AC == "yes":
                        return int(tem.per_km*km*(3/2)+150)
                    return tem.per_km*km+150
                return tem.per_km*km

    # payment frame for customers

    def pay(self, amount, root):
        if amount == 0:
            return True
        frame = tk.Frame(root,
                         width="625",
                         height="400",
                         bg="purple3")
        frame.place(relx=0.2, rely=0.2)
        text = ""
        if amount > 0:
            text += "pay"
        else:
            amount *= -1
            text += "refund"
        label = tk.Label(frame, text=str(float(amount)) +
                         "RS", font=("Arial", 12))
        label.place(relx=0.2, rely=0.3)
        button = tk.Button(frame, text=text, borderwidth=3, relief=tk.GROOVE, font=(
            "Arial", 12), command=lambda: self.payment_done(frame, amount, text))
        button.place(relx=0.45, rely=0.3)
        return True

    # manage list of master object on return of car
    def return_vehicle(self, tem):
        tem.repair = "yes"
        tem.rent = "no"
        tem.available = "no"
        self.on_repair_cars.append(tem)
        for i in range(len(self.on_rent_cars)):
            if tem.id == self.on_rent_cars[i].id:
                self.on_rent_cars.pop(i)
                return

    # disconnect customer to car after return of car

    def free_customer(self, tem):
        self.customers[self.logged_in_customer_index].car_rented_id = -1
        self.customers[self.logged_in_customer_index].rented_car_index = -1
        self.customers[self.logged_in_customer_index].rented_car_index_second = -1
        self.customers[self.logged_in_customer_index].time_car_rented = 0
        self.customers[self.logged_in_customer_index].time_to_return = 0

    # payment done message

    def payment_done(self, frame, pay, text):
        messagebox.showinfo("Payment", "Transfer successfull!")

        # sending mail
        self.mails.append(
            [self.customers[self.logged_in_customer_index].email, pay, datetime.datetime.now(), text])

        frame.destroy()
