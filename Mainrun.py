# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("PhoneOS")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when
# button is clicked
def clicked():
    root.destroy()
    execfile('signup.py')
    

def click():
    root.destroy()
    execfile('signin.py')
    

 
# button widget with red color text inside
btn = Button(root, text = "Sign Up" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)
 
btn = Button(root, text = "Sign In" ,
             fg = "red", command=click)
# Set Button Grid
btn.grid(column=2, row=5)


# Execute Tkinter
root.mainloop()

