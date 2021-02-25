from src.classes.RentalSoftware import *
from src.screens.start import *
from src.screens.loading import *
import tkinter as tk
from PIL import ImageTk, Image
from src import do_exit


def main():
    print("main")
    name, owner, owner_ph, helpline = get_last()
    head = RentalSoftware(name, owner, owner_ph, helpline)
    root = tk.Tk()
    root.title(head.name)
    root.geometry("1100x700")
    img = Image.open(r"src/img/bg.jpg")
    img = ImageTk.PhotoImage(img)
    root.iconphoto(False, img)
    root.resizable(width=False, height=False)
    loading(root)
    canvas = tk.Canvas(root, width=1100, height=700)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(r"src/img/new.jpg").resize((1100, 700)))
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    head.__fetch__()
    start(root, head)
    print(len(head.all_cars), end=" cars loaded!\n")
    root.protocol("WM_DELETE_WINDOW", lambda: do_exit.do_exit(root, head))
    root.bind("<Escape>", lambda e: do_exit.do_exit(root, head))
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
