#!/usr/bin/python

# Test button options

#====================================

from Tkinter import *

class GIFError(Exception): pass
def get_gif_num_frames(filename):
    frames = 0
    with open(filename, 'rb') as f:
        if f.read(6) not in ('GIF87a', 'GIF89a'):
            raise GIFError('not a valid GIF file')
        f.seek(4, 1)
        def skip_color_table(flags):
            if flags & 0x80: f.seek(3 << ((flags & 7) + 1), 1)
        flags = ord(f.read(1))
        f.seek(2, 1)
        skip_color_table(flags)
        while True:
            block = f.read(1)
            if block == ';': break
            if block == '!': f.seek(1, 1)
            elif block == ',':
                frames += 1
                f.seek(8, 1)
                skip_color_table(ord(f.read(1)))
                f.seek(1, 1)
            else: raise GIFError('unknown block type')
            while True:
                l = ord(f.read(1))
                if not l: break
                f.seek(l, 1)
    return frames



class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        Button(self, bitmap="error").grid(row=0, column=0, padx=5)
        Button(self, bitmap="gray75").grid(row=0, column=1, padx=5)
        Button(self, bitmap="gray50").grid(row=0, column=2, padx=5)

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
        self.quitButton.grid(row=0, column=20, padx=5)
        
	self.photo_path = "/home/pi/Downloads/giphy.gif"

        self.photo = PhotoImage(self,
            file = self.photo_path, format="gif -index 2"
        )
	self.canvas = Canvas(self,
	    image = self.photo
	    )
	#self.label.grid(row=1,column=0,padx=5,pady=5)

app = Application()
app.top = app.winfo_toplevel()
app.top.title("This is my second GUI")
app.top.geometry("700x500-0-0")
app.top.minsize(700,500)
app.top.maxsize(700,500)

print get_gif_num_frames("/home/pi/Downloads/giphy.gif")

app.mainloop()

