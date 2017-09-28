#!/usr/bin/python

# Test text entry and error capture

#====================================

from Tkinter import *
import tkMessageBox

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.grid()
        self.createWidgets()
    def msg(self):
        tkMessageBox.showinfo("Hey", "msg")
    def calc(self):
        self.field3.delete(0,END)
        self.field3.insert(0,int(self.field1.get())+int(self.field2.get()))



    def createWidgets(self):
        Label(self, text="+").grid(row=0, column=2, padx=5)
        Label(self, text="=").grid(row=0, column=4, padx=5)

        self.field1 = Entry(self)
	self.field1.grid(row=0, column=1, padx=5)
        self.field2 = Entry(self)
	self.field2.grid(row=0, column=3, padx=5)
        self.field3 = Entry(self)
	self.field3.grid(row=0, column=5, padx=5)

        self.evalButton = Button (
            self,
            text="Calculate",
            bd=3,
	    bg="tomato",
            padx=10,
            pady=20,
            command=self.calc,
            underline=2,
	    activebackground="red"
            )
        self.quitButton = Button (
            self,
            text="Quit",
            bd=3,
	    bg="tomato",
            padx=10,
            pady=20,
            command=self.quit,
            underline=2,
	    activebackground="red"
            )
        self.evalButton.grid(row=0, column=10, padx=5)
        self.quitButton.grid(row=0, column=20, padx=5)
        
app = Application()
app.top = app.winfo_toplevel()
app.top.title("This is my second GUI")
app.top.geometry("700x500-0-0")
app.top.minsize(700,500)
app.top.maxsize(700,500)


app.mainloop()

