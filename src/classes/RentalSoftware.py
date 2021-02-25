from src.classes.vehical import *
import pandas as pd
class RentalSoftware:
    name = ""
    owner_name = ""
    owner_phone_number = ""
    help_line_number = ""
    all_cars = []
    on_rent_cars = []
    on_repair_cars = []
    availabel_cars = []
    general_data = []
    #all cars
    #on rent cars
    #on repair cars
    #av.

    def __init__(self, name, ownername, ownerphn, helplinen):
        self.name = name
        self.owner_name = ownername
        self.owner_phone_number = ownerphn
        self.help_line_number = helplinen
        self.all_cars.clear()
        self.on_rent_cars.clear()
        self.on_repair_cars.clear()
        self.availabel_cars.clear()

    def __fetch__(self):
        data = pd.read_excel(r'.\cache\all.xlsx')
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
        g_data = pd.read_excel(r'./cache/general.xlsx')
        g_data = pd.DataFrame(g_data, columns=['model',
                                               'nonAC',
                                               'AC'])
        self.general_data.clear()
        for i in range(len(g_data)):
            self.general_data.append((g_data['model'][i], g_data['nonAC'][i], g_data['AC'][i]))