from tkinter import *

root = Tk()

popup = Menu(root, tearoff=0)
popup.add_command(label="Main Product")
popup.add_command(label="Side Product")

def popupm(bt):
     try:         
        x = bt.winfo_rootx()
        y = bt.winfo_rooty()
        popup.tk_popup(x, y, 0)
     finally:
           popup.grab_release()

bt = Button(root, text='Menu')
bt.configure(command = lambda: popupm(bt))
bt.place(x = 10, y = 15)

root.mainloop()