from src.classes.RentalSoftware import *
from src.screens.start import *
from src.screens.loading import *
import tkinter as tk


def main():
    print("main")
    head = RentalSotware("agk", "Abhishek", "100", "101")
    root = tk.Tk()
    root.title("agk")
    root.geometry("1100x700")
    loading(root)
    head.__fetch__()
    start(root, head)
    root.mainloop()
    print("done")


main()
