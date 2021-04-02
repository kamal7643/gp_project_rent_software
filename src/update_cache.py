import pandas as pds
import xlsxwriter as xw


# updating excel files of cars and customers
def update_cache(head):
    # update car's file
    if head.cars_changes != 0:
        final = xw.Workbook('./cache/cars.xlsx')
        wsh = final.add_worksheet()
        # header
        wsh.write(0, 0, 'id')
        wsh.write(0, 1, 'model')
        wsh.write(0, 2, 'repair')
        wsh.write(0, 3, 'rent')
        wsh.write(0, 4, 'available')
        wsh.write(0, 5, 'prize')
        wsh.write(0, 6, 'times_rented')
        wsh.write(0, 7, 'times_repaired')
        wsh.write(0, 8, 'pay_for_repair')
        wsh.write(0, 9, 'gain')
        wsh.write(0, 10, 'rented_for')
        wsh.write(0, 11, 'rented_time')
        wsh.write(0, 12, 'milli_meter_reading_on_rent')
        wsh.write(0, 13, 'AC')
        wsh.write(0, 14, 'advance')
        wsh.write(0, 15, 'per_hour')
        wsh.write(0, 16, 'per_km')
        # body
        for i in range(len(head.all_cars)):
            wsh.write(i+1, 0, head.all_cars[i].id)
            wsh.write(i+1, 1, head.all_cars[i].model)
            wsh.write(i+1, 2, head.all_cars[i].repair)
            wsh.write(i+1, 3, head.all_cars[i].rent)
            wsh.write(i+1, 4, head.all_cars[i].available)
            wsh.write(i+1, 5, head.all_cars[i].prize)
            wsh.write(i+1, 6, head.all_cars[i].times_rented)
            wsh.write(i+1, 7, head.all_cars[i].times_repaired)
            wsh.write(i+1, 8, head.all_cars[i].pay_for_repair)
            wsh.write(i+1, 9, head.all_cars[i].gain)
            wsh.write(i+1, 10, head.all_cars[i].rented_for)
            wsh.write(i+1, 11, head.all_cars[i].rented_time)
            wsh.write(i+1, 12, head.all_cars[i].milli_meter_reading_on_rent)
            wsh.write(i+1, 13, head.all_cars[i].AC)
            wsh.write(i+1, 14, head.all_cars[i].advance)
            wsh.write(i+1, 15, head.all_cars[i].per_hour)
            wsh.write(i+1, 16, head.all_cars[i].per_km)
        final.close()
    # update customer's file

    if head.customers_changes != 0:
        final = xw.Workbook('./cache/customers.xlsx')
        wsh = final.add_worksheet()
        # header
        wsh.write(0, 0, 'id')
        wsh.write(0, 1, 'name')
        wsh.write(0, 2, 'phone_number')
        wsh.write(0, 3, 'email')
        wsh.write(0, 4, 'licence')
        wsh.write(0, 5, 'car_rented_id')
        wsh.write(0, 6, 'rented_car_index')
        wsh.write(0, 7, 'rented_car_index_second')
        wsh.write(0, 8, 'time_rented')
        wsh.write(0, 9, 'time_to_return')
        wsh.write(0, 10, 'payment')
        wsh.write(0, 11, 'username')
        wsh.write(0, 12, 'password')
        # body
        for i in range(len(head.customers)):
            wsh.write(i + 1, 0, head.customers[i].id)
            wsh.write(i + 1, 1, head.customers[i].name)
            wsh.write(i + 1, 2, head.customers[i].phone_number)
            wsh.write(i + 1, 3, head.customers[i].email)
            wsh.write(i + 1, 4, head.customers[i].driving_licence)
            wsh.write(i + 1, 5, head.customers[i].car_rented_id)
            wsh.write(i + 1, 6, head.customers[i].rented_car_index)
            wsh.write(i + 1, 7, head.customers[i].rented_car_index_second)
            wsh.write(i + 1, 8, head.customers[i].time_car_rented)
            wsh.write(i + 1, 9, head.customers[i].time_to_return)
            wsh.write(i + 1, 10, head.customers[i].payment)
            wsh.write(i + 1, 11, head.customers[i].username)
            wsh.write(i + 1, 12, head.customers[i].password)
        final.close()
        print("all files updated")
