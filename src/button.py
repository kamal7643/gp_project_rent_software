from src.screens import about
from src.screens import customer
from src.screens import admin
from src.screens import help
from src.screens import start
from src.screens import admin_action
from src.screens import admin_show
from src.screens import get_rent
from src.screens import return_frame
from src.screens import setting
from src import do_exit
import winsound
import tkinter as tk


def button(root, head, f_name):
    if head.sound == "on":
        winsound.Beep(600, 100)
    if f_name == "about":
        about.about(root, head)
    elif f_name == "customer":
        customer.customer(root, head)
    elif f_name == "admin":
        admin.admin(root, head)
    elif f_name == "do_exit":
        do_exit.do_exit(root, head)
    elif f_name == "help":
        help.help(root, head)
    elif f_name == "start":
        start.start(root, head)
    elif f_name == "admin_action":
        admin_action.admin_action(root, head)
    elif f_name == "admin_show":
        admin_show.admin_show(root, head)
    elif f_name == "get_rent":
        get_rent.get_rent(root, head)
    elif f_name == "return_frame":
        return_frame.return_frame(root, head)
    elif f_name == "setting":
        setting.setting(root, head)