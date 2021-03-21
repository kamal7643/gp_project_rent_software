

class Customer:
    id = ""
    name = ""
    phone_number = ""
    email = ""
    driving_licence = ""
    car_rented_id = ""
    time_car_rented = ""
    time_to_return = ""
    payment = 0
    password = ""

    def __init__(self, id):
        self.id = id

    def profile(self, name, phn, email, driving_l, car_id, time_car_rented, time_to_return, payment, password):
        self.name = str(name)
        self.phone_number = str(phn)
        self.email = str(email)
        self.driving_licence = str(driving_l)
        self.car_rented_id = car_id
        self.time_car_rented = time_car_rented
        self.time_to_return = time_to_return
        self.payment = payment
        self.password = str(password)

    def return_status(self):
        return self.car_rented

    def payment_status(self):
        return self.payment
