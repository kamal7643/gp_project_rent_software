from src import update_cache
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
from src.screens import loading
import urllib.request


# exit application
def do_exit(root, head):
    if messagebox.askquestion("Access Required", "Are you sure to quit?") == 'yes':
        # update owner and history related files
        update_last(head)

        # update excel files of cars and customers
        update_cache.update_cache(head)
        # sending mails
        loading.loading(root)
        if len(head.mails) != 0:
            if connect():
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(head.email_id, head.email_password)
                for i in head.mails:
                    msg = EmailMessage()
                    msg.set_content('your payment of '+str(i[1])+'Rs is done!\non:'+str(i[2].hour) + '/' + str(
                        i[2].minute) + '\tdate:' + str(i[2].day)+'/'+str(i[2].month)+'/'+str(i[2].year))
                    msg['Subject'] = 'Payment done for TAAS '+str(i[3])
                    msg['From'] = 'kswami848@gmail.com'
                    msg['To'] = i[0]
                    server.send_message(msg)
                server.quit()
            else:
                messagebox.showerror(
                    "not connected", "you are not connected to internet to send emails")

        # quit the application(master window)
        quit()

# network connection check


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


# function to update owner file and history file
def update_last(head):
    # update owner file
    if head.history_changes != 0:
        f = open("cache\storage.txt", "w")
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
