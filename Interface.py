#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import Tkinter as tk
import ttk #Like the css for tkinter

LARGE_FONT=("Verdana", 12)

class Sense_Pro(tk.Tk):

    def __init__(self,*args,**kwargs): #base arguments and keyword arguments
        tk.Tk.__init__(self,*args,**kwargs)
        #tk.Tk.iconbitmap(self, default='image/icon.ico) ERROR <FIXME> 
        tk.Tk.wm_title(self, "Sense_Pro") #Set Title

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True) #If item is less then pack
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} #create empty dictionary

        for F in (StartPage, GraphPage):

            frame = F(container,self) #call StartPage

            self.frames[F] = frame #add StartPage to dictionary

            frame.grid(row=0, column=0, sticky="nsew") #north south east west

        self.show_frame(StartPage) #initialised StartPage
        
    def show_frame(self, cont):
        frame = self.frames[cont] #look through the dictionary
        frame.tkraise()   #raise the window to the front

    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Graph Page",
                            command= lambda:controller.show_frame(GraphPage))
        button1.pack()


class GraphPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back to Home Page",
                            command= lambda:controller.show_frame(StartPage))
        button2.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8,9],[2,5,7,8,4,3,4,6,6])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = Sense_Pro()
app.mainloop()
