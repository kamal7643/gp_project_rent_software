from src import update_cache
from tkinter import messagebox


# exit application
def do_exit(root, head):
    if messagebox.askquestion("Access Required", "Are you sure to quit?") == 'yes':
        # update owner and history related files
        update_last(head)
        # update excel files of cars and customers
        update_cache.update_cache(head)
        # quit the application(master window)
        quit()


# function to update owner file and history file
def update_last(head):
    # update owner file
    f = open("cache\storage.txt","w")
    f.write(head.name+"\n")
    f.write(head.owner_name+"\n")
    f.write(head.owner_phone_number+"\n")
    f.write(head.help_line_number+"\n")
    f.write(head.sound+"\n")
    f.write(head.bg_file_name+"\n")
    f.write(head.password+"\n")
    f.close()
    # update history file
    f = open("cache\history.txt", "w")
    for i in head.history:
        f.write(i+"\n")
    f.close()
    print("cache txt files updated")
