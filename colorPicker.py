from tkinter import *
import win32gui
import PIL.ImageGrab
from win32api import GetKeyState, GetAsyncKeyState
import time

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
	
class MyGUI:
    def __init__(self, root):
        self.root = root
        root.title("Color picker")
        root.resizable(False,False)
        root.geometry("250x80")

        self.label = Label(root, text="Color rgb:", width=15).grid(row=0, column=0)
        self.labelRGB = Label(root, text="#")
        self.labelRGB.grid(row=0, column=1)
		
        self.label = Label(root, text="Color hex:").grid(row=1, column=0)
        self.labelHEX = Label(root, text="#")
        self.labelHEX.grid(row=1, column=1)

        self.colorBox = Entry(bg='#ffffff')
        self.colorBox.grid(row=2, column=1)
		
        self.pick_button = Button(root, text="Pick color", command=self.get_pixel)
        self.pick_button.grid(row=2, column=0)
		
    def get_pixel(self):
        # '0x01' is code for left mouse button
        while True:
            if(GetAsyncKeyState(0x01) < 0): break
            time.sleep(0.01)
			
        _,_,(x,y) = win32gui.GetCursorInfo()
        (r,g,b) = PIL.ImageGrab.grab().load()[x, y]
        self.set_color(r,g,b)
			
    def set_color(self, r, g, b):
        self.colorBox['bg'] = rgb2hex(r,g,b)
        self.labelRGB['text'] = "R: %s; G: %s; B: %s" % (r,g,b)
        self.labelHEX['text'] = rgb2hex(r,g,b)
        self.root.clipboard_clear()
        self.root.clipboard_append(rgb2hex(r,g,b))

root = Tk()
my_gui = MyGUI(root)
root.mainloop()