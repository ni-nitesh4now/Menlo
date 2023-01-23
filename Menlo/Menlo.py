from tkinter.filedialog import askopenfilename
import pandas as pd
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

root = Tk()
main=Menu(root)
root.title("Tez Software")

begval=DoubleVar()
begval.set(0.00)
endval=DoubleVar()
endval.set(1)
avgval=IntVar()

width= root.winfo_screenwidth()
height= root.winfo_screenheight()
w1=25
h=2
background="#d3eaf2"
font="arial 11"
left=20
v = StringVar()

root.configure(bg=background)
root.geometry("%dx%d" % (width, height))

def display_selected():
    #Label(text=f'You selected {var.get()}',font=('sans-serif', 14)).pack()
    Label(text=f'You selected').pack()

def Trigger_input():
    user_input = simpledialog.askstring("Pop up for user input!", "What do you want to ask the user to input here?")
    if user_input != "":
        print(user_input)


class MyWindow:
    def __init__(self, win):
        x0, xt0, y0 = 10, 100, 50
        sig=list()
        menu2=Canvas(win,width=width,height=40).pack()
        #----- Import Buttons-----------        
        # self.btn2 = Button(menu2, text='Reset Averaging',height=h,width=w1)
        self.btn2 = Button(menu2, text='Select CSV File',height=h,width=w1)
        self.btn2.bind('<Button-1>', self.import_csv_data)
        self.btn2.place(x=0,y=0)
        #---- Start button -------
        self.btn1 = Button(menu2, text='Start measurement',height=h,width=w1)
        self.btn1.bind('<Button-1>', self.start)
        self.btn1.place(x=210,y=0)
                #----- Buttons-----------        
        self.btn3 = Button(menu2, text='Hold',height=h,width=w1)
        self.btn3.bind('<Button-1>', self.nothing)
        self.btn3.place(x=420,y=0)
                #----- Buttons-----------        
        self.btn4 = Button(menu2, text='Find Pulse',height=h,width=w1)
        self.btn4.bind('<Button-1>', self.nothing)
        self.btn4.place(x=630,y=0)
                #----- Buttons-----------        
        self.btn5 = Button(menu2, text='Enable Antena Voltage',height=h,width=w1)
        self.btn5.bind('<Button-1>', self.nothing)
        self.btn5.place(x=840,y=0)
                #----- Buttons-----------        
        self.btn6 = Button(menu2, text='Enable Lasers',height=h,width=w1)
        self.btn6.bind('<Button-1>', self.nothing)
        self.btn6.place(x=1050,y=0)
                #----- Buttons-----------        
        self.btn7 = Button(menu2, text='Config Lasers',height=h,width=w1)
        self.btn7.bind('<Button-1>', self.nothing)
        self.btn7.place(x=1260,y=0)

        #label
        self.lbll = Label(root,text="Measurement Setup", font=font,bg=background)
        self.lbll.place(x=left,y=60)

        #---- First label and entry -------
        self.lbl0 = Label(win, text='Begin:',font=font,bg=background)
        self.lbl0.place(x=left,y=100)
        self.t0 = Spinbox(root,textvariable=begval,width=10,bd=2,font=20,from_=-500,to=500,increment=0.1)
        self.t0.place(x=100,y=100)

        #---- Second label and entry -------
        self.lbl1 = Label(win,text='End',font=font,bg=background)
        self.lbl1.place(x=left+280,y=100)
        self.t1 = Spinbox(root,textvariable=endval,width=10,bd=2,font=20,from_=begval.get(),to=500,increment=0.1)
        self.t1.place(x=350,y=100)

        Label(root,text='No. of avarages',font=font,bg=background).place(x=left+480,y=100)
        self.avg=Spinbox(root,textvariable=avgval,width=10,bd=2,font=20,from_=1,to=500,increment=1,command=display_selected)
        self.avg.place(x=650,y=100)

        #------ Figure----------
        self.figure = Figure(figsize=(18.5,6))
        self.figure.patch.set_facecolor(background)
        #---- subplot 1 -------
        self.TimeDomain = self.figure.add_subplot(121)
        self.TimeDomain.set_xlim(begval.get(), endval.get())
        self.TimeDomain.set_title('Time Domain')
        self.TimeDomain.set_xlabel("Time(ps)")
        self.TimeDomain.set_ylabel("Amplitude")

        self.TimeDomain.grid('on')
        #---- subplot 2 -------
        self.FrequencyDomain = self.figure.add_subplot(1,2,2)
        self.FrequencyDomain.set_xlim(begval.get(), endval.get())
        self.FrequencyDomain.set_title('Frequency Domain')
        self.FrequencyDomain.grid('on')
        self.FrequencyDomain.set_xlabel("Frequency(THz)")
        self.FrequencyDomain.set_ylabel("Intensity(dB)")
        
        #---- Show the plot-------
        self.plots = FigureCanvasTkAgg(self.figure, win)
        self.plots.get_tk_widget().place(x =-220,y=150)

        #-----------Tool Bar--------------#
        self.frame1 = tk.Frame(root)
        self.toolbar = NavigationToolbar2Tk(self.plots, self.frame1)
        self.frame1.place(x=left,y=150)
        self.plots.get_tk_widget().place(x =-160,y=150)
    
    def import_csv_data(self,event):
        csv_file_path = askopenfilename()
        print(csv_file_path)
        df = pd.read_csv(csv_file_path)
        self.sig=list(df.signal)

    def computefft(self):
        Fs = 16
        t = np.arange(0,len(self.sig),1)
        x=self.sig
        n = np.size(t)
        fr = (Fs/2)*np.linspace(0,1,len(self.sig))
        # Compute FFT 
        X = fft(x)
        X_m = (2/n)*abs(X[0:np.size(fr)])
        fr=list(fr)
        X_m=list(X_m)
        return fr,X_m,t,X

    def start(self, event):
        fr, X_m,t,X = self.computefft()
        self.TimeDomain.set_xlim(0,len(self.sig))
        self.TimeDomain.plot(t, self.sig, 'r', lw=2.5)
        self.FrequencyDomain.set_xlim(0,8)
        self.FrequencyDomain.plot(fr, X_m, 'b', lw=2.5)
        self.plots.draw()
 
    def nothing(self, event):
        Label(text='You selected').pack()

mywin = MyWindow(root)

#------------Menu bar--------------------#

file=Menu(main,tearoff=0)
sub_menu1 = Menu(file, tearoff=0)
sub_menu1.add_command(label='Keyboard Shortcuts')
sub_menu1.add_command(label='Color Themes')
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

Help=Menu(main,tearoff=0)
Help.add_command(label='Show log')
Help.add_command(label='About us..')

root.config(menu=main)
main.add_cascade(label='File',menu=file)

root.config(menu=main)
main.add_cascade(label='Measurement',menu=Measurement)

root.config(menu=main)
main.add_cascade(label='Hardware',menu=Hardware)

root.config(menu=main)
main.add_cascade(label='Data Processing',menu=DataP)

root.config(menu=main)
main.add_cascade(label='Help',menu=Help)
root.mainloop()
