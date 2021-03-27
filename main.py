from src.classes.RentalSoftware import *
from src.screens.start import *
from src.screens.loading import *
import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
from src import do_exit
from src.screens import help
from src.screens import admin
from src.screens import customer


def main():
    print("main")
    name, owner, owner_ph, helpline, sound, bg_file_name, pin = get_last()
    head = RentalSoftware(name, owner, owner_ph, helpline, sound, bg_file_name, pin)
    root = tk.Tk()
    root.title(head.name)
    root.geometry("1100x700")
    img = Image.open(r"src/img/main_icon.jpg")
    img = ImageTk.PhotoImage(img)
    root.iconphoto(False, img)
    root.resizable(width=False, height=False)
    loading(root)
    canvas = tk.Canvas(root, width=1100, height=700)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(r"src/img/" +
                                        head.bg_file_name).resize((1100, 700)).filter(ImageFilter.BoxBlur(1)))
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    head.__fetch__()
    start(root, head)
    print(len(head.all_cars), end=" cars loaded!\n")
    root.protocol("WM_DELETE_WINDOW", lambda: do_exit.do_exit(root, head))
    root.bind("<Escape>", lambda e: do_exit.do_exit(root, head))
    root.bind("<Control-Key-m >", lambda e: start(root, head))
    root.bind("<Control-Key-` >", lambda e: help.help(root, head))
    root.bind("<Control-Key-d >", lambda e: admin.admin(root, head))
    root.bind("<Control-Key-u >", lambda e: customer.customer(root, head))
    root.configure(cursor="arrow")
    root.mainloop()


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


main()
