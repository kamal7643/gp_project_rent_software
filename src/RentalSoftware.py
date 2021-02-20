from src.vehical import *
import pandas as pd
class RentalSotware:
    name=""
    ownerName=""
    ownerPhoneNumber=""
    helpLineNumber=""
    all_cars=[]
    on_rent_cars=[]
    on_repair_cars=[]
    availabel_cars=[]
    #all cars
    #on rent cars
    #on repair cars
    #av.
    def __init__(self,name,ownername,ownerphn,helplinen):
        self.name=name
        self.ownerName=ownername
        self.ownerPhoneNumber=ownerphn
        self.helpLineNumber=helplinen
    def __fetch__(self):
        data = pd.read_excel(r'C:\Users\kamal swami\PycharmProjects\pythonProject\cache\all.xlsx')
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
                                           'mili_meter_reading_on_rent',
                                           'AC',
                                           'advance'])
        for i in range(len(data)):
            temp=vehical(i)
            temp.id=data['id'][i]
            temp.model=data['model'][i]
            temp.repair=data['repair'][i]
            temp.rent=data['rent'][i]
            temp.available=data['available'][i]
            temp.prize=data['prize'][i]
            temp.times_rented=data['times_rented'][i]
            temp.times_repaired=data['times_repaired'][i]
            temp.pay_for_repair=data['pay_for_repair'][i]
            temp.gain=data['gain'][i]
            temp.rented_for=data['rented_for'][i]
            temp.rented_time=data['rented_time'][i]
            temp.mili_meter_reading_on_rent=data['mili_meter_reading_on_rent'][i]
            temp.AC=data['AC'][i]
            temp.advance=data['advance'][i]
            self.all_cars.append(temp)
            if temp.repair=="yes":
                self.on_repair_cars.append(temp)
            if temp.rent=="yes":
                self.on_rent_cars.append(temp)
            if temp.available=="yes":
                self.availabel_cars.append(temp)
# times_rented=0
#     times_repaired=0
#     pay_for_repair=0
#     gain=0
#     rented_for=""
#     rented_time=""
#     mili_meter_reading_on_rent=0.0
#     AC=False