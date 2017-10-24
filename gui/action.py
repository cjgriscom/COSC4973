#!/usr/bin/python

# Demo for sliding scale

#====================================

from Tkinter import *

class SimpleApplication(Frame):
   def mouseDown(self, event):
       self.lastX = event.x
       self.lastY = event.y

   def mouseMove(self, event):
       self.draw.move(CURRENT, event.x - self.lastX, event.y - self.lastY)
       self.lastX = event.x
       self.lastY = event.y
        
   def mouseEnter(self, event):
       self.draw.itemconfig(CURRENT, fill="red")


   def mouseLeave(self, event):
       self.draw.itemconfig(CURRENT, fill="blue")

   def createWidgets(self):
       times24 = tkFont.Font(family="times", size="24")
       times36 = tkFont.Font(family="times", size="36")
       self.draw = Canvas(self, width="300", height="200")
       self.draw.grid(row=0)
       self.draw.create_rectangle(1,1,300,200)

       self.QUIT = Button(self, text="Quit", foreground="red", bd=10,
                          font=times24, command=self.quit)
       self.QUIT.grid(row=1, sticky=N+S+E+W)

       fred = self.draw.create_oval(0,0,20,20,fill="green",tags="selected")

       self.draw.tag_bind(fred, "<Any-Enter>", self.mouseEnter)
       self.draw.tag_bind(fred, "<Any-Leave>", self.mouseLeave)

       Widget.bind(self.draw, "<1>", self.mouseDown)
       Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)
       
       self.ck1Var = intVar()
       self.ck1Var.set(0)
       self.ck1 = Checkbutton(self, text="Off", font=times24, 
                              command=self.__ck1Handler, variable=self.ck1Var)
       self.ck1Id = self.draw.create_window(100,100,anchor=NW,window=self.ck1)

#not finished \/
       self.ck2Var = intVar()
       self.ck2Var.set(1)
       self.ck2 = Checkbutton(self, text="On", font=times24, 
                              command=self.__ck1Handler, variable=self.ck1Var)
       self.ck2Id = self.draw.create_window(100,100,anchor=NW,window=self.ck1)





   def __init__(self):
       createWidgets(self)


app = SimpleApplication()
#Create an instance of the class SimpleApplication
app.mainloop()
