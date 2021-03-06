#!/usr/bin/python

# Demo for sliding scale

#====================================

from Tkinter import *

class SimpleApplication(Frame):
    
    
    def print_value(self, val):
        print "slider now at ", val
    def reset(self):
        self.slider.set(0)
    
    def __init__(self):
        Frame.__init__(self)
	self.pack()
        self.slider = Scale(self, {"from":0,
	                           "to":100,
				   "orient":"horizontal",
				   "length":"3i",
                                   "command":self.print_value})
        self.reset = Button(self, {"text":"reset slider",
	                           "command":self.reset})
        self.done = Button(self, {"text":"Quit",
	                          "fg":"red",
				  "command":self.quit})
	self.slider.pack({"side":"top"})
        
	self.reset.pack({"side":"top", "fill":"both"})
	self.done.pack({"side":"top", "fill":"both"})
	#Almopst doen

app = SimpleApplication()
#Create an instance of the class SimpleApplication
app.mainloop()
