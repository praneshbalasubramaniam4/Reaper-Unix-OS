
import tkinter as signup
  
roo=signup.Tk()
 
# setting the windows size
roo.geometry("600x400")
roo.title("Sign Up")
  
# declaring string variable
# for storing name and password
name_var=signup.StringVar()
passw_var=signup.StringVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
     
    name_var.set("")
    passw_var.set("")

    my_file = open("credintals.txt","w+")
    my_file.write(name)
    my_file.write('\n')
    my_file.write(password)
    roo.destroy()
    execfile('mainos.py')

     
# creating a label for
# name using widget Label
name_label = signup.Label(roo, text = 'Username', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = signup.Entry(roo,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a label for password
passw_label = signup.Label(roo, text = 'Password', font = ('calibre',10,'bold'))
  
# creating a entry for password
passw_entry=signup.Entry(roo, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=signup.Button(roo,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
roo.mainloop()