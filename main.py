from src.classes.RentalSoftware import *
from src.screens.start import *
from src.screens.loading import *
import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
from src import do_exit
from src.screens import help
from src.screens import admin
from src.screens import customer


# here is the main function (or starting function ) of the application
def main():
    print("main")
    # getting owner's information from cache files
    name, owner, owner_ph, helpline, sound, bg_file_name, pin = get_last()
    # here is the system object named head
    head = RentalSoftware(name, owner, owner_ph, helpline,
                          sound, bg_file_name, pin)
    # master window
    root = tk.Tk()
    root.title(head.name)
    root.geometry("1100x700")
    # adding icon to master window
    img = ImageTk.PhotoImage(Image.open(
        r"src/img/bg.png").resize((1200, 1000)))
    root.iconphoto(False, img)
    # fix size of master window
    root.resizable(width=False, height=False)
    # if fetch data takes longer time
    loading(root)
    # initializing memory for cars and customers
    head.__fetch__()
    # adding background image to master window
    canvas = tk.Canvas(root, width=1100, height=700)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(r"src/img/" +
                                        head.bg_file_name).resize((1100, 700)).filter(ImageFilter.BoxBlur(1)))
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    # start page is the landing page for software
    start(root, head)
    print(len(head.all_cars), end=" cars loaded!\n")
    # handling unexpected terminate condition
    # do_exit function will update storage files for the software
    root.protocol("WM_DELETE_WINDOW", lambda: do_exit.do_exit(root, head))
    # adding some shortcut keys to master window
    root.bind("<Escape>", lambda e: do_exit.do_exit(root, head))
    root.bind("<Control-Key-m >", lambda e: start(root, head))
    root.bind("<Control-Key-` >", lambda e: help.help(root, head))
    root.bind("<Control-Key-d >", lambda e: admin.admin(root, head))
    root.bind("<Control-Key-u >", lambda e: customer.customer(root, head))
    root.configure(cursor="arrow")
    root.mainloop()


# get owner information stored in files
def get_last():
    f = open("cache\\storage.txt", "r")
    name = f.readline()
    owner = f.readline()
    owner_ph = f.readline()
    helpline = f.readline()
    sound = f.readline()
    bg_file_name = f.readline()
    pin = f.readline()
    f.close()
    return name[:-1], owner[:-1], owner_ph[:-1], helpline[:-1], sound[:-1], bg_file_name[:-1], pin[:-1]


# calling main function of the software
main()
