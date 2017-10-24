#!/usr/bin/python

# Demo for canvas

#====================================

from Tkinter import *


window = Tk()
window.title('Layout Example using .pack')

lbl_red=Label(window, width=30, height=15, bg='red')
lbl_grn=Label(window, width=12, height=5, bg='green')
lbl_blu=Label(window, width=12, height=5, bg='blue')
lbl_yel=Label(window, width=12, height=5, bg='yellow')

lbl_red.pack(side=TOP)
lbl_grn.pack(side=BOTTOM, fill=X) # fill all x
lbl_blu.pack(side=LEFT)
lbl_yel.pack(side=RIGHT)


window1 = Tk()
window1.title('Layout Example Using .grid')

lbl_red_2=Label(window1, width=30, height=15, bg='red')
lbl_grn_2=Label(window1, width=12, height=5, bg='green')
lbl_blu_2=Label(window1, width=12, height=5, bg='blue')
lbl_yel_2=Label(window1, width=12, height=5, bg='yellow')

lbl_red_2.grid(row=1, column=1)
lbl_grn_2.grid(row=2, column=2) # fill all x
lbl_blu_2.grid(row=3, column=3)
lbl_yel_2.grid(row=1, column=1)


window2 = Tk()
window2.title('Layout Example Using .place')


lbl_red_3=Label(window2, width=30, height=15, bg='red')
lbl_grn_3=Label(window2, width=12, height=5, bg='green')
lbl_blu_3=Label(window2, width=12, height=5, bg='blue')
lbl_yel_3=Label(window2, width=12, height=5, bg='yellow')

lbl_red_3.place(x=10,y=10)
lbl_grn_3.place(x=36,y=45)
lbl_blu_3.place(x=63,y=80)
lbl_yel_3.place(x=90,y=115)

window.mainloop()
window1.mainloop()
window2.mainloop()
