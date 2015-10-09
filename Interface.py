#!/usr/bin/env python

import Tkinter as tk

LARGE_FONT=("Verdana", 12)

class Sense_Pro(tk.Tk):

    def __init__(self,*args,**kwargs): #base arguments and keyword arguments
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True) #If item is less then pack

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} #create empty dictionary

        for F in (StartPage, Page1):

            frame = F(container,self) #call StartPage

            self.frames[F] = frame #add StartPage to dictionary

            frame.grid(row=0, column=0, sticky="nsew") #north south east west

        self.show_frame(StartPage) #initialised StartPage
        
    def show_frame(self, cont):
        frame = self.frames[cont] #look through the dictionary
        frame.tkraise()   #raise the window to the front

def qf(string):
    print (string)
    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="visit Page 1",
                            command= lambda:controller.show_frame(Page1))
        button1.pack()

class Page1(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page1", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Back to Home Page",
                            command= lambda:controller.show_frame(StartPage))
        button2.pack()

app = Sense_Pro()
app.mainloop()
