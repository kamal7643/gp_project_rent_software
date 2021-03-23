class vehical:
    id = ""
    model = ""
    repair = ""
    rent = ""
    available = ""
    prize = 100000.0
    times_rented = 0
    times_repaired = 0
    pay_for_repair = 0
    gain = 0
    rented_for = 0
    rented_time = ""
    milli_meter_reading_on_rent = 0.0
    AC = ""
    advance = 0
    per_hour = 0
    per_km = 0

    def __init__(self, i):
        self.id = i
