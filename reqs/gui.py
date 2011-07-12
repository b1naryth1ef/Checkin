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

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())
 
# create needed widgets
label = Label(root, text=s)
entry = Entry(root, width=25)
button = Button(root, text="Update", command=update)
text = Text(root, width=25, height=1)
 
# place the widgets in a grid
label.grid(row=10, column=11)
entry.grid(row=10, column=12)
button.grid(row=10, column=13)
text.grid(row=11, column=11)
 
# put the cursor into entry field
entry.focus()
 
root.mainloop()