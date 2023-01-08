import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

root = tk.Tk()
root.title("I am a newbie!")

# create the figure instances
fig = Figure()
a = fig.add_subplot(122)
b = fig.add_subplot(121)

# figure1 has two subplot and figure 2 has only one
fig2 = Figure(figsize=(2, 2))
c = fig2.add_subplot(111)

# toolbar for canvas1 (figure1)
frame1 = tk.Frame(root)
canvas = FigureCanvasTkAgg(fig, root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, frame1)
frame1.pack(side=tk.TOP, fill=tk.X)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.X)

button = tk.Button(master=root, text='Quit')
button.pack(side=tk.TOP)


# put this to the bottom

frame2 = tk.Frame(root)
canvas2 = FigureCanvasTkAgg(fig2, root)
toolbar2 = NavigationToolbar2Tk(canvas2, frame2)
frame2.pack(side=tk.TOP, fill=tk.X)
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.X)
# toolbar for canvas2 (figure2)



# this function just to exit
def _quit():
    root.quit()
    root.destroy()


button = tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=tk.BOTTOM)

root.mainloop()