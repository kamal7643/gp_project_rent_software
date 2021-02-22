import pandas as pds
import xlsxwriter as xw


def update_cache(head):
    final = xw.Workbook('./cache/all.xlsx')
    wsh = final.add_worksheet()
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
    # final = pds.DataFrame({'id': [1, 2],
    #                        'model': [1, 2],
    #                        'repair': [1, 2],
    #                        'rent': [1, 2],
    #                        'available': [1, 2],
    #                        'prize': [1, 2],
    #                        'times_rented': [1, 2],
    #                        'times_repaired': [1, 2],
    #                        'pay_for_repair': [1, 2],
    #                        'gain': [1, 2],
    #                        'rented_for': [1, 2],
    #                        'rented_time': [1, 2],
    #                        'milli_meter_reading_on_rent': [1, 2],
    #                        'AC': [1, 2],
    #                        'advance': [1, 2],
    #                        'per_hour': [1, 2],
    #                        'per_km': [1, 2]})
    # final = pds.concat(final, pds.DataFrame(id[3]))
    # for i in head.all_cars:
    #     final['id'].append(i.id)
    #     final['model'].append(i.model)
    #     final['repair'].append(i.repair)
    #     final['rent'].append(i.rent)
    #     final['available'].append(i.available)
    #     final['prize'].append(i.prize)
    #     final['times_rented'].append(i.times_rented)
    #     final['times_repaired'].append(i.times_repaired)
    #     final['pay_for_repair'].append(i.pay_for_repair)
    #     final['gain'].append(i.gain)
    #     final['rented_for'].append(i.rented_for)
    #     final['rented_time'].append(i.rented_time)
    #     final['milli_meter_reading_on_rent'].append(i.milli_meter_reading_on_rent)
    #     final['AC'].append(i.AC)
    #     final['advance'].append(i.advance)
    #     final['per_hour'].append(i.per_hour)
    #     final['per_km'].append(i.per_km)
    # final.to_excel('./final.xlsx', index=False)
    print("excel files updated")