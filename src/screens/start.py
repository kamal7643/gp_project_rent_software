from src.screens import clear
from src.screens import customer
from src import button
import tkinter as tk


# landing page to the software
def start(root, head):
    print("start")
    clear.clear(root)
    # about software button
    about_button = tk.Button(text="About", width="12", background="gray80", font=("Arial Bold", 10),
                             command=lambda: button.button(root, head, "about"))
    about_button.place(relx=0.0, rely=0.9)
    # go to customer page
    customer_button = tk.Button(text="customer", width="20", background="blue", font=("Arial Bold", 12),
                                command=lambda: customer_wants(root, head))
    # go to Admin page
    admin_button = tk.Button(text="Admin", width="20", background="blue", font=("Arial Bold", 12),
                             command=lambda: admin_wants(root, head))
    customer_button.place(relx=0.40, rely=0.35)
    admin_button.place(relx=0.40, rely=0.45)
    restart_buttton = tk.Button(text="restart", width="12", background="gray80", font=("Arial Bold", 10),
                                command=lambda: button.button(root, head, "restart"))
    restart_buttton.place(relx=0.91, rely=0.85)
    # exit application
    exit_button = tk.Button(text="exit", width="12", background="gray80", font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "do_exit"))
    exit_button.place(relx=0.91, rely=0.9)


# redirecting admin (login page or admin home page)
def admin_wants(root, head):
    if head.logged_in == "yes":
        button.button(root, head, "admin")
    else:
        button.button(root, head, "login")


# redirection customer (login page or customer home page)
def customer_wants(root, head):
    if head.logged_in_customer == "yes":
        customer.customer(root, head)
    else:
        button.button(root, head, "login_customer")
