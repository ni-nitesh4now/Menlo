from tkinter import *

def display_selected():
    Label(text=f'You selected {float(var.get())}',font=('sans-serif', 14),bg='#6393A6').pack()

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200')
ws.config(bg='#6393A6')

var = DoubleVar()
Spinbox(ws,textvariable=var,from_=-500,to=500,increment=0.0001,command=display_selected,font=('sans-serif', 18), ).pack(pady=20)

ws.mainloop()