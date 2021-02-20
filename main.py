from src.RentalSoftware import *
from src.start import *
import  tkinter as tk
def main():
    head=RentalSotware("agk","abhi","100","101")
    root=tk.Tk()
    root.title("agk")
    root.geometry("1100x700")
    start(root)
    root.mainloop()
    print("done")




main()
