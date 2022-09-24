# Python Ver:   3.5.1
#
# Author:       Jalen Allison
#
# Purpose:      Student Tracking Assignment. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationship
#
# Tested OS:    This code was written and tested to work with Windows 10.
# NOT DONE YET

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Be sure to import our other modules
# so we can have access to them
import tracking_gui
import tracking_func


# Frame is the Tkinter frame clas that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        tracking_func.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: tracking_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        tracking_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()  #syntax to create window from tkinter
    App = ParentWindow(root) #connecting the class and tkinter
    root.mainloop() #continously runs so it stays up until it is physically exited out of 
