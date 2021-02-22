from src import update_cache


def do_exit(root, head):
    store_last(head)
    update_cache.update_cache(head)
    quit()


def store_last(head):
    f = open("cache\storage.txt","w")
    f.write(head.name+"\n")
    f.write(head.owner_name+"\n")
    f.write(head.owner_phone_number+"\n")
    f.write(head.help_line_number+"\n")
    f.close()
    print("cache txt files updated")
