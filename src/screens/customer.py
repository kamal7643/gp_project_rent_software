from src.screens.clear import *
from src.screens import login_customer
from tkinter import messagebox
from src import button
import tkinter as tk
from PIL import ImageTk, Image

# customer home page


def customer(root, head):
    # if customer not logged in
    if head.logged_in_customer != "yes":
        messagebox.showerror("Access denied", "Please log in!")
        login_customer.login_customer(root, head)
    else:
        print("customer")
        clear(root)

        # profile of cutomer
        profile_button = tk.Button(text="profile", width="10", font=("Arial", 12), borderwidth=3, relief=tk.GROOVE,
                                   command=lambda: profile_show(root, head))
        profile_button.place(relx=0.01, rely=0.01)

        # go to rent page
        rent_button = tk.Button(text="rent", width="20", background="blue", font=("Arial Bold", 12), borderwidth=3, relief=tk.GROOVE,
                                command=lambda: button.button(root, head, "get_rent"))

        # go to renturn car page
        return_button = tk.Button(text="return", width="20", background="blue", font=("Arial Bold", 12), borderwidth=3, relief=tk.GROOVE,
                                  command=lambda: button.button(root, head, "return_frame"))
        rent_button.place(relx=0.40, rely=0.35)
        return_button.place(relx=0.40, rely=0.45)

        # go back to landing page
        back_button = tk.Button(text="back", width="12", background="gray80", font=("Arial Bold", 10), borderwidth=3, relief=tk.GROOVE,
                                command=lambda: button.button(root, head, "start"))
        back_button.place(relx=0.0, rely=0.9)

        # exit application
        exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10), borderwidth=3, relief=tk.GROOVE,
                                command=lambda: button.button(root, head, "do_exit"))
        exit_button.place(relx=0.91, rely=0.9)

        # go to landing page
        home_button = tk.Button(text="home", width="12", background="gray80", font=("Arial Bold", 10), borderwidth=3, relief=tk.GROOVE,
                                command=lambda: button.button(root, head, "start"))
        home_button.place(relx=0.45, rely=0.9)

        # delete current logged in account
        delete_account = tk.Button(text="Delete Account", width="15", font=("Arial", 10), borderwidth=3, relief=tk.GROOVE,
                                   command=lambda: delete_ac(head, root))
        delete_account.place(relx=0.85, rely=0)

        # logged out this account
        log_out_button = tk.Button(text="Logout", width="15", font=("Arial", 10), borderwidth=3, relief=tk.GROOVE,
                                   command=lambda: logout(root, head))
        log_out_button.place(relx=0.85, rely=0.07)


# if payment is done and no car rented to this customer(current logged in)
def delete_ac(head, root):
    g = head.get_customer(head.customer_id)
    if g:

        # if current logged in account not connected with any car and payment is done
        if g.car_rented_id == -1 and g.payment == 0:
            if messagebox.askquestion("Are You Sure?", "Delete this Account!") == "yes":
                print(g.id)
                if head.delete_customer(head.customer_id):
                    head.history.append("account deleted")
                    head.history_changes += 1
                    head.logged_in_customer = "no"
                    head.customer_id = -1
                    button.button(root, head, "start")
                else:
                    messagebox.showerror(
                        "Error", "Facing some error while deleting account")
            else:
                print("here")
        else:
            messagebox.showerror(
                "Error", "You can not delete account without done payment")
    else:
        messagebox.showerror("Error", "please restart software")

# logged out current logged in accout of customer


def logout(root, head):
    head.logged_in_customer = "no"
    head.customer_id = -1
    button.button(root, head, "start")


# profile show frame
def profile_show(root, head):
    frame = tk.Frame(root, width="225", height="150", bg="purple", borderwidth = 10)
    frame.place(relx=0.04, rely=0.1)
    text = ""
    i = head.logged_in_customer_index
    text += "username = "+head.customers[i].username
    text += "\n"
    text += "name = "+head.customers[i].name+"\n"
    text += "Email = "+head.customers[i].email+"\n"
    text = text.replace("@gmail.com", " ")
    text += "Contact Number = "+head.customers[i].phone_number+"\n"
    label = tk.Label(frame, text=text, font=("Arial", 10),
                     width="30", justify=tk.LEFT, anchor='nw', bg="purple")
    label.place(relx=0.01, rely=0.01)
    back_button = tk.Button(frame, text="back", borderwidth=3, relief=tk.GROOVE, font=(
        "Arail", 12), command=lambda: frame.destroy())
    back_button.place(relx=0.01, rely=0.8)
