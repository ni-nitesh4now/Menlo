import tkinter  as tk 
my_w = tk.Tk()
my_w.geometry("250x120")  

def my_fun():
    pass

menubar = tk.Menu(my_w)
my_font1=('Times',12,'bold')
menu_file = tk.Menu(menubar,title='my title' ,
    tearoff=1,fg='red',bg='yellow') # file
menu_edit=tk.Menu(menubar,tearoff=0)  # edit menu 
menu_sub=tk.Menu(menu_file,tearoff=0,bg='green')
menu_file.add_cascade(label='Sub 1',menu=menu_sub ) # add sub
menu_sub.add_command(label='Sub 11',command=my_fun()) 
menu_sub.add_command(label='Sub 12',command=my_fun())

menubar.add_cascade(label="File", menu=menu_file) # Top Line
menubar.add_cascade(label="Edit", menu=menu_edit) # Top Line

menu_file.add_command(label="New", command=my_fun()) # Item 1 of file
menu_file.add_command(label="Open..", command=my_fun()) # Item 2  
menu_file.add_separator()

menu_file.add_command(label="Exit", command=my_w.quit) # Item 3  
menu_edit.add_command(label="Undo", command=my_fun())# Item 1 of Edit 
menu_edit.add_command(label="Redo", command=my_fun())# Item 2 of Edit 

menu_sub2=tk.Menu(menu_sub,tearoff=0,bg='red')
menu_sub.add_cascade(label='Sub 2',menu=menu_sub2)
menu_sub2.add_command(label='Sub 21',command=my_fun())
menu_sub2.add_command(label='Child ',command=lambda:my_child())

my_w.config(menu=menubar) # adding menu to window
my_w.mainloop()