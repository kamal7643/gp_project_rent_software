

class Customer:
    id = ""
    name = ""
    phone_number = ""
    email = ""
    driving_licence = ""
    car_rented = ""
    time_car_rented = ""
    time_to_return = ""
    payment = 0

    def __init__(self, id):
        self.id = id

    def profile(self, name, phn, email, driving_l):
        self.name = name
        self.phone_number = phn
        self.email = email
        self.driving_licence = driving_l

    def return_status(self):
        return self.car_rented

    def payment_status(self):
        return self.payment