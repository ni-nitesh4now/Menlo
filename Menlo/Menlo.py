import pyautogui as pag
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
from math import pi
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


#---------definitions------------------#

root=Tk()
main=Menu(root)
def donothing():
    return
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
w1=25
h=2
background="#d3eaf2"
font="arial 11"
left=20
plt.close('all')
root.geometry("%dx%d" % (width, height))
root.configure(bg=background)
root.title("Tez Software")
def display_selected():
    #Label(text=f'You selected {var.get()}',font=('sans-serif', 14)).pack()
    Label(text=f'You selected').pack()

begval=DoubleVar()
begval.set(-333.00)
endval=DoubleVar()
avgval=IntVar()

def Trigger_input():
    user_input = simpledialog.askstring("Pop up for user input!", "What do you want to ask the user to input here?")
    if user_input != "":
        print(user_input)

# Generate sine wave
Fs = 300
t = np.arange(0,1,1/Fs)
f = 20
x = np.sin(2*pi*f*t)+0.5*np.sin(2*pi*40*t)+ 1.5*np.sin(2*pi*5*t)

n = np.size(t)
fr = (Fs/2)*np.linspace(0,1,n//2)
# Compute FFT 
X = fft(x)
X_m = (2/n)*abs(X[0:np.size(fr)])


menu= StringVar()
menu.set("Select Any Language")

menu2=Canvas(root,width=width,height=50).pack()
Button(menu2,text="Start measurement",height=h,width=w1, command=display_selected).place(x=0,y=0)
Button(menu2,text="Reset Averaging",height=h,width=w1).place(x=210,y=0)
Button(menu2,text="Hold",height=h,width=w1).place(x=420,y=0)
Button(menu2,text="Find Pulse",height=h,width=w1).place(x=630,y=0)
Button(menu2,text="Enable Antena Voltage",height=h,width=w1).place(x=840,y=0)
Button(menu2,text="Enable Lasers",height=h,width=w1).place(x=1050,y=0)
Button(menu2,text="Config Lasers",height=h,width=w1).place(x=1260,y=0)

#label
Label(root,text="Measurement Setup", font=font,bg=background).place(x=left,y=60)

Label(root,text='Begin:',font=font,bg=background).place(x=left,y=100)
begin=Spinbox(root,textvariable=begval,width=10,bd=2,font=20,from_=-500,to=500,increment=0.1)
begin.place(x=100,y=100)

Label(root,text='End',font=font,bg=background).place(x=left+280,y=100)
end=Spinbox(root,textvariable=endval,width=10,bd=2,font=20,from_=-500,to=500,increment=0.1)
end.place(x=350,y=100)

Label(root,text='No. of avarages',font=font,bg=background).place(x=left+480,y=100)
avg=Spinbox(root,textvariable=avgval,width=10,bd=2,font=20,from_=1,to=500,increment=1,command=display_selected)
avg.place(x=650,y=100)

#------------------figures---------------------#

fig = plt.Figure(figsize=(18.5,6.5))
TimeDomain = fig.add_subplot(121)
fig.patch.set_facecolor(background)
TimeDomain.set_title('Time Domain')
TimeDomain.set_xlim(0,1)
TimeDomain.set_ylim(-3,3)
lines = TimeDomain.plot([],[])[0]
lines.set_xdata(t)
lines.set_ydata(x)
TimeDomain.grid('on')
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.draw() # A tk.DrawingArea.

frequencyDomain = fig.add_subplot(1,2,2)
frequencyDomain.set_title('Frequency Domain')
frequencyDomain.set_xlim(0,80)
frequencyDomain.set_ylim(0,3)
lines1 = frequencyDomain.plot([],[])[0]
lines1.set_xdata(fr)
lines1.set_ydata(X_m)
frequencyDomain.grid('on')
plt.tight_layout()

#-----------Tool Bar--------------#
frame1 = tk.Frame(root)
toolbar = NavigationToolbar2Tk(canvas, frame1)
frame1.place(x=left,y=150)
canvas.get_tk_widget().place(x =-220,y=150)

#-----------------------------------------Menu part-------------------------------------------------------#

  
file=Menu(main,tearoff=0)
sub_menu1 = Menu(file, tearoff=0)
sub_menu1.add_command(label='Keyboard Shortcuts')
sub_menu1.add_command(label='Color Themes')
# i=1
# file.add_cascade(label="Save As",menu=sub_menu1, state=NORMAL if i==1 else DISABLED)
file.add_cascade(label="Save As",menu=sub_menu1, state=DISABLED)
file.add_command(label='Open')


Measurement=Menu(main,tearoff=0)
mask = Menu(Measurement, tearoff=0)
mask.add_command(label='Trigger',command=Trigger_input)
Measurement.add_command(label='Start Measurement',command=display_selected)
Measurement.add_command(label='Reset Averaging')
Measurement.add_separator()
Measurement.add_command(label='Hold')
Measurement.add_command(label='Find Pulse')
Measurement.add_cascade(label='Mask',menu=mask)

Hardware=Menu(main,tearoff=0)
Hardware.add_command(label="Enable Antena Voltage")
Hardware.add_command(label="Enable Laser")
Hardware.add_command(label="Configure Laser")

DataP=Menu(main,tearoff=0)
DataP.add_command(label="Optimize time")
DataP.add_command(label="Axis Parameter")

help=Menu(main,tearoff=0)
help.add_command(label='Show log')
help.add_command(label='About us..')

root.config(menu=main)
main.add_cascade(label='File',menu=file)

root.config(menu=main)
main.add_cascade(label='Measurement',menu=Measurement)

root.config(menu=main)
main.add_cascade(label='Hardware',menu=Hardware)

root.config(menu=main)
main.add_cascade(label='Data Processing',menu=DataP)

root.config(menu=main)
main.add_cascade(label='Help',menu=help)
#-------------------------------------------------------------------------------------------------------------# 

root.mainloop()