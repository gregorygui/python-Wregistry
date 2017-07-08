'''
Created on 9 juil. 2017

@author: Gregory
'''
import tkinter
from tkinter import Menu, BOTH

from gui.StartPage import StartPage
from gui.UserPage import UserPage
from gui.ComputerPage import ComputerPage         

class MainApp(tkinter.Tk):
    """Application container for different frames"""
    
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        tkinter.Tk.wm_title(self, "Windows Forensic")
        self.menuBar()
        self.config(pady="5")
        
        container=tkinter.Frame(self)
        container.pack(fill=BOTH, expand=1)
        self.center_window()
        
        self.frames = {}
        
        for F in (StartPage, ComputerPage, UserPage):
            page_name=F.__name__
            frame=F(parent=container, controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        frame=self.frames[page_name]
        frame.tkraise()      
        
    def center_window(self):
        w=1000
        h=500
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        
        self.geometry('%dx%d+%d+%d' % (w,h,x,y))
        
    def menuBar(self):
        menubar=Menu(self)
        
        menubar.add_command(label="Home", command=lambda:self.show_frame("StartPage"))
        menubar.add_command(label="Exit", command=self.quit)
        menubar.add_command(label="?", command=self.quit)
       
        self.config(menu=menubar)        