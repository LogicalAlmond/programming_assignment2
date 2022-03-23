from tkinter import *
from turtle import back
from webbrowser import BackgroundBrowser

# config root
root = Tk()
root.geometry('500x500')
root.columnconfigure(1, weight=1)
root.rowconfigure(5, weight=1)
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

# Button
send_button = Button(root, text='Send')
send_button.grid(row=99, column=1, sticky='e', padx=3, pady=3, ipadx=2, ipady=2)

#m Message
message_label = Label(root, text='Message: ', font=("Arial", 14), background='#d7d6d5')
message_label.grid(row=4, column=0, sticky='wesn', padx=2, pady=2)
message = Text(root)
message.grid(row=5, column=0, columnspan=2, padx=8, pady=3)

# mainFrame = Frame(root, width=500, height=500)

# titleLabel = Label(root, text="Simple Email Client")
# titleLabel.pack(side=TOP)

# senderFrame = Frame(mainFrame)
# ccFrame = Frame(mainFrame)
# msgFrame = Frame(mainFrame)

# senderLabel = Label(senderFrame, text='To: ')
# senderEntry = Entry(senderFrame)

# ccLabel = Label(ccFrame, text='CC: ')
# ccEntry = Entry(ccFrame)

# msgLabel = Label(msgFrame, text='Message: ',bd=0)
# msgText = Text(msgFrame, bg="light yellow")



# senderFrame.pack()
# senderLabel.pack(side=LEFT)
# senderEntry.pack(side=RIGHT)

# ccFrame.pack()
# ccLabel.pack(side=LEFT)
# ccEntry.pack(side=RIGHT)

# msgFrame.pack(padx=40, pady=40)
# msgLabel.pack(side=TOP)
# msgText.pack(side=BOTTOM, padx=1, pady=1)

# mainFrame.pack()
root.mainloop()
