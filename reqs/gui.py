#! /usr/bin/env python
from Tkinter import *
import tkMessageBox
import main, db

def update():
    data = entry.get()
    x = db.osearch("name",data)
    db.checkin(x.id)
    #text.delete(1.0, END)
    text.insert(INSERT, "User: %s was checked in!" % (data))
    entry.delete(0, END)
 
root = Tk()
 
# for testing
s = "Check in:"

 
# create needed widgets
label = Label(root, text=s)
entry = Entry(root, width=25)
button = Button(root, text="Update", command=update)
text = Text(root, width=25, height=1)
 
# place the widgets in a grid
label.grid(row=1, column=1)
entry.grid(row=1, column=2)
button.grid(row=1, column=3)
text.grid(row=2, column=1)
 
# put the cursor into entry field
entry.focus()
 
root.mainloop()