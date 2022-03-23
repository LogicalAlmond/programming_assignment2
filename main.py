from cgitb import text
from tkinter import *
from turtle import back
from webbrowser import BackgroundBrowser

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
send_button = Button(root, text='Send')
send_button.grid(row=99, column=1, sticky='e', padx=3, pady=3, ipadx=2, ipady=2)

# Attach Button
attach_button = Button(root, text='Attach')
attach_button.grid(row=99, column=0, columnspan=1, sticky='we', padx=3, pady=3, ipadx=2, ipady=2)

#m Message
message_label = Label(root, text='Message: ', font=("Arial", 14), background='#d7d6d5')
message_label.grid(row=4, column=0, sticky='wesn', padx=2, pady=2)
message = Text(root)
message.grid(row=5, column=0, columnspan=2, padx=8, pady=3)


root.mainloop()
