from src.RentalSoftware import *
from src.loading import *
from src.start import *
import  tkinter as tk
def main():
    head=RentalSotware("agk","abhi","100","101")
    root=tk.Tk()
    root.title("agk")
    root.geometry("1100x700")
    loading(root) # for more amount of data
    head.__fetch__()
    start(root,head)
    root.mainloop()
    print("done")




main()
