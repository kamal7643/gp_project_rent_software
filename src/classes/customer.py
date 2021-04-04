
# CUSTOMER CLASS AND ITS METHODS
# class for customer objects
class Customer:
    id = ""
    name = ""
    phone_number = ""
    email = ""                  #for user login and signup
    driving_licence = ""
    car_rented_id = -1
    rented_car_index = -1
    rented_car_index_second = -1
    time_car_rented = ""
    time_to_return = ""
    payment = 0
    username = ""
    password = ""

    # init of customers

    def __init__(self, id):
        self.id = id

    # set customer profile

    def profile(self, name, phn, email, driving_l, car_id, car_index, car_index_second, time_car_rented, time_to_return, payment, username, password):
        self.name = str(name)
        self.phone_number = str(phn)
        self.email = str(email)
        self.driving_licence = str(driving_l)
        self.car_rented_id = int(car_id)
        self.rented_car_index = int(car_index)
        self.rented_car_index_second = car_index_second
        self.time_car_rented = int(time_car_rented)
        self.time_to_return = time_to_return
        self.payment = payment
        self.username = str(username)
        self.password = str(password)

    # check car status linked to customer

    def return_status(self):
        return self.car_rented_id

    # check payment status

    def payment_status(self):
        return self.payment
