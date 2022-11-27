# Import Module
from tkinter import *

root = Tk()
root.title("PhoneOS")
root.geometry('350x200')



def clicked():
    root.destroy()
    execfile('signup.py')
    

def click():
    root.destroy()
    execfile('signin.py')
    

 
btn = Button(root, text = "Sign Up" ,
             fg = "black", command=clicked)
btn.grid(column=2, row=0)
 
btn = Button(root, text = "Sign In" ,
             fg = "black", command=click)
btn.grid(column=2, row=6)


# Execute Tkinter
root.mainloop()

