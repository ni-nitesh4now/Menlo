from tkinter import *
import tkinter as tk
my_w = tk.Tk()
my_w.geometry("250x120") 
a=2
def my_child():
    my_w_child=Toplevel(my_w) # Child window 
    my_w_child.geometry("200x200")  # Size of the window 
    my_w_child.title("www.plus2net.com")
    my_str1 = tk.StringVar()
    l1 = tk.Label(my_w_child,  textvariable=my_str1 )
    l1.grid(row=1,column=2) 
    my_str1.set("Hi I am Child window")
    
menubar = tk.Menu(my_w)
menu_file = tk.Menu(menubar,tearoff=0) # file
menu_edit=tk.Menu(menubar,tearoff=0)  # edit menu 
menubar.add_cascade(label="File", menu=menu_file) # Top Line
menubar.add_cascade(label="Edit", menu=menu_edit) # Top Line
menu_file.add_command(label="New window", command=lambda:my_child())
menu_file.add_command(label="Exit", command=my_w.quit)
my_w.config(menu=menubar) # adding menu to window
my_w.mainloop()