from src import update_cache
from tkinter import messagebox


def do_exit(root, head):
    if messagebox.askquestion("Access Required", "Are you sure to quit?") == 'yes':
        store_last(head)
        update_cache.update_cache(head)
        quit()


def store_last(head):
    f = open("cache\storage.txt","w")
    f.write(head.name+"\n")
    f.write(head.owner_name+"\n")
    f.write(head.owner_phone_number+"\n")
    f.write(head.help_line_number+"\n")
    f.write(head.sound+"\n")
    f.write(head.bg_file_name+"\n")
    f.write(head.password+"\n")
    f.close()
    f = open("cache\history.txt", "w")
    for i in head.history:
        f.write(i+"\n")
    f.close()
    print("cache txt files updated")
