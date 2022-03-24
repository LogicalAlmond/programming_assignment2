from re import sub
from tkinter import *
from tkinter import messagebox
from mailHandler import MailHandler

EMAIL_ADDR = 'almondjoyforlyfe@gmail.com'
PASSWD = 'thisismypassword123'
SMTP_SERVER = 'smtp.gmail.com'
PORT = 587

mailer = MailHandler(EMAIL_ADDR, PASSWD, SMTP_SERVER, PORT)
mailer.login()

def onClickSend():
    email = recv_entry.get()
    subject = sub_entry.get()
    msg = message.get('1.0', END)
    mailer.send(subject, msg, email)
    print('Message sent.')
    messagebox.showinfo('Email sent', 'you clicked me!')

# config root
root = Tk()
root.geometry('500x500')
root.columnconfigure(1, weight=10)
root.rowconfigure(5, weight=10)
root.configure(background='#d7d6d5')

#Receiver
recv_label = Label(root, text='To:', font=('Arial', 14), background='#d7d6d5')
recv_label.grid(sticky='we', padx=5, pady=5)
recv_entry = Entry(root)
recv_entry.grid(row=0,column=1, sticky='ew', padx=8, pady=3)

# CC
cc_label = Label(root, text='CC:', font=('Arial', 14), background='#d7d6d5')
cc_label.grid(row=1, column=0, sticky='we', padx=2, pady=2)
cc_entry = Entry(root)
cc_entry.grid(row=1,column=1, sticky='ew', padx=8, pady=3)

#subject
sub_label = Label(root, text='Subject:', font=('Arial', 14), background='#d7d6d5')
sub_label.grid(row=2, column=0, sticky='we', padx=2, pady=2)
sub_entry = Entry(root)
sub_entry.grid(row=2,column=1, sticky='ew', padx=8, pady=3)

# Send Button
send_button = Button(root, text='Send', activebackground='#93a3c2', command=buttonClick)
send_button.grid(row=99, column=1, sticky='e', padx=3, pady=3, ipadx=2, ipady=2)

# Attach Button
attach_button = Button(root, text='Attach', activebackground='#93a3c2')
attach_button.grid(row=99, column=0, sticky='we', padx=3, pady=3, ipadx=2, ipady=2)

#m Message
message_label = Label(root, text='Message: ', font=("Arial", 14), background='#d7d6d5')
message_label.grid(row=4, column=0, sticky='wesn', padx=2, pady=2)
message = Text(root)
message.grid(row=5, column=0, columnspan=2, padx=8, pady=3)


root.mainloop()

# Code stuffs
# mailer = MailHandler('almondjoyforlyfe@gmail.com', 'thisismypassword123', 'smtp.gmail.com', 587)
# mailer.login()
