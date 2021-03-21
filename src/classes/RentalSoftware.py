from src.classes.vehical import *
from src.classes.customer import *
import pandas as pd


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
    password = ""
    all_cars = []
    on_rent_cars = []
    on_repair_cars = []
    availabel_cars = []
    general_data = []
    customers = []
    history = []

    def __init__(self, name, owner_name, owner_phn, Helpline, sound, bg_file_name, pin):
        self.name = name
        self.owner_name = owner_name
        self.owner_phone_number = owner_phn
        self.help_line_number = Helpline
        self.sound = sound
        self.bg_file_name = bg_file_name
        self.all_cars.clear()
        self.on_rent_cars.clear()
        self.on_repair_cars.clear()
        self.availabel_cars.clear()
        self.password = pin

    def __fetch__(self):
        data = pd.read_excel(r'.\cache\cars.xlsx')
        data = pd.DataFrame(data, columns=['id',
                                           'model',
                                           'repair',
                                           'rent',
                                           'available',
                                           'prize',
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

        self.availabel_cars.clear()
        self.all_cars.clear()
        self.on_rent_cars.clear()
        self.on_repair_cars.clear()
        for i in range(len(data)):
            temp = vehical(i)
            temp.id = data['id'][i]
            temp.model = data['model'][i]
            temp.repair = data['repair'][i]
            temp.rent = data['rent'][i]
            temp.available = data['available'][i]
            temp.prize = data['prize'][i]
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
                self.availabel_cars.append(temp)
        customer_data = pd.read_excel(r'./cache/customers.xlsx')
        customer_data = pd.DataFrame(customer_data, columns=['id',
                                                             'name',
                                                             'phone_number',
                                                             'email',
                                                             'licence',
                                                             'car_rented_id',
                                                             'time_rented',
                                                             'time_to_return',
                                                             'payment',
                                                             'password'])
        self.general_data.clear()
        self.customers.clear()
        for i in range(len(customer_data)):
            temp = Customer(customer_data['id'][i])
            temp.profile(customer_data['name'][i],
                         customer_data['phone_number'][i],
                         customer_data['email'][i],
                         customer_data['licence'][i],
                         customer_data['car_rented_id'][i],
                         customer_data['time_rented'][i],
                         customer_data['time_to_return'][i],
                         customer_data['payment'][i],
                         customer_data['password'][i])
            self.customers.append(temp)
        self.history.clear()
        f = open("cache\\history.txt", "r")
        line = f.readline()
        while line:
            self.history.append(line[:-1])
            line = f.readline()

    def is_admin(self, password):
        if self.password == password:
            self.logged_in = "yes"
            return True
        else:
            return False

    def is_customer(self, password):
        for i in self.customers:

            if i.password == password:
                self.logged_in_customer = "yes"
                self.customer_id = i.id
                return True

    def is_double_customer(self, other):
        for i in self.customers:
            if i.email == other.email or i.phone_number == other.phone_number:
                return True
        return False

    def is_possible_password(self, password):
        for i in self.customers:
            if i.password == password:
                return False
        return True

    def delete_customer(self, id):
        for i in range(len(self.customers)):
            if self.customers[i].id == id:
                self.customers.pop(i)
                self.history.append("Account deleted!")
                return True
        return False

    def get_customer(self, id):
        for i in self.customers:
            if i.id == id:
                return i
        return None
