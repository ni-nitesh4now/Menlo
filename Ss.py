import pyautogui as pag
from tkinter import *
from tkinter import filedialog

root=Tk()

main=Menu(root)

def donothing():
    return

def takess():
    myScreenshot=pag.screenshot()
    filep=filedialog.asksaveasfilename(defaultextension=".png")
    myScreenshot.save(filep)

canvass=Canvas(root,width=300,height=300)
canvass.pack()

myB=Button(text='Take SS',command=takess,bg='blue',fg='white')
canvass.create_window(150,150,window=myB)

#-----------------------------------------Menu part-------------------------------------------------------#

file=Menu(main,tearoff=0)
file.add_command(label='Open',command=donothing)
file.add_command(label='Save')
file.add_command(label='Save As')
file.add_command(label='Close')
file.add_command(label='cdcn')
file.add_command(label='eden')

edit=Menu(main,tearoff=0)
edit.add_command(label='DSF')
edit.add_command(label='DSfrfF')
edit.add_command(label='DfSF')
edit.add_separator()
edit.add_command(label='DF')

help=Menu(main,tearoff=0)
help.add_command(label='Sorry Cant help')

root.config(menu=main)
main.add_cascade(label='File',menu=file)

root.config(menu=main)
main.add_cascade(label='Edit',menu=edit)

root.config(menu=main)
main.add_cascade(label='Help',menu=help)
#-------------------------------------------------------------------------------------------------------------# 

root.mainloop()