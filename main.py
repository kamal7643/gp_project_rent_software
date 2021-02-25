from src.classes.RentalSoftware import *
from src.screens.start import *
from src.screens.loading import *
import tkinter as tk
from PIL import ImageTk, Image


def main():
    print("main")
    name, owner, owner_ph, helpline = get_last()
    head = RentalSoftware(name, owner, owner_ph, helpline)
    root = tk.Tk()
    root.title(head.name)
    root.geometry("1100x700")
    img = ImageTk.PhotoImage(Image.open(r"src/img/bg.jpg"))
    root.iconphoto(False, img)
    root.resizable(width=False, height=False)
    loading(root)
    head.__fetch__()
    start(root, head)
    print(len(head.all_cars), end=" cars loaded!\n")
    root.mainloop()


def get_last():
    f = open("cache\storage.txt", "r")
    name = f.readline()
    owner = f.readline()
    owner_ph = f.readline()
    helpline = f.readline()
    f.close()
    return name[:-1], owner[:-1], owner_ph[:-1], helpline[:-1]


main()
