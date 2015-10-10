#!/usr/local/bin/python
#SENSE_PRO
#         ______  ______  ____     ______  ______
#        /  ___/ /  ___/ /    \   /  ___/ /  ___/
#       /  /__  /  /__  /  /\  \ /  /__  /  /__ 
#      /__   / /   __/ /  / /  //__   / /   __/
#     ___/  / /   /__ /  / /  /___/  / /   /__
#    /_____/ /______//__/ /__//_____/ /______/
#
#
#
#
#Auth: LeoYong
#Reference: Sentdex youtube channel
#Description: Interface 
#FIXME: Cuztomize Sensor Page
#   

#----------------matplotlib backend imports
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

#---------------------------------------matplotlib imports
import matplotlib.animation as animation
from matplotlib import style

#-------------------TKinter imports
import Tkinter as tk
import ttk #Like the css for tkinter

import Sensor


#-------------------------Global
LARGE_FONT=("Verdana", 12)
style.use("ggplot") # graph style
Light = Sensor.Sensor(23)
SenseDat = list()
IndexDat = list()
index = 0
f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111) #default



#--------------Animate Graph
def animate(i):  
    Data = Light.Read_Analog()
    global index
    index = index +1
    print Data
    SenseDat.append(Data)
    IndexDat.append(index)
    #---------------Move view frame
    if (index > 50):
        SenseDat.pop(0)
        IndexDat.pop(0)
    a.clear()
    a.plot(IndexDat,SenseDat,'g', label="Lights")

    title = "Sensor Data"
    a.set_title(title)
    

#======================Main Interface Class           
class Sense_Pro(tk.Tk):
    
    def __init__(self,*args,**kwargs): #Base arguments and keyword arguments
        tk.Tk.__init__(self,*args,**kwargs)
        #tk.Tk.iconbitmap(self, default='image/icon.ico) ERROR <FIXME> 
        tk.Tk.wm_title(self, "Sense_Pro") #Set Title

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True) #If item is less then pack
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} #Create empty dictionary of frames

        for F in (StartPage, GraphPage):

            frame = F(container,self) 

            self.frames[F] = frame #Add page to dictionary

            frame.grid(row=0, column=0, sticky="nsew") #North south east west

        self.show_frame(StartPage) #Show StartPage 1st
        
    def show_frame(self, cont):
        frame = self.frames[cont] #look through the dictionary
        frame.tkraise()   #raise the window to the front
        
#=========================END CLASS
        
        
#=========================Start Page Class    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="""
          SENSE_PRO <alpha>
    
    This application is free to use.
    Use this application at your own risk""", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Sensor Page",
                            command= lambda:controller.show_frame(GraphPage))
        button.pack()

#=========================END CLASS
        
        
#=========================Sensor Page Class   
class GraphPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Sensor Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #----------------------------------Graph widget
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

          
        button = ttk.Button(self, text="Back to Home Page",
                            command= lambda:controller.show_frame(StartPage))
        button.pack()
        
#=========================END CLASS



app = Sense_Pro()
ani = animation.FuncAnimation(f, animate, interval=100)
app.mainloop()
