'''
Created on 9 juil. 2017

@author: Gregory
'''
import tkinter
from tkinter import Menu
from tkinter.constants import BOTH, N, E, W, S

from gui.StartPage import StartPage
from gui.UserListPage import UserListPage
from gui.ComputerPage import ComputerPage         

class MainApp(tkinter.Tk):
    """Application container for different frames"""
    
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        tkinter.Tk.wm_title(self, "Windows Forensic")
        self.menuBar()
        
        container=tkinter.Frame(self)
        container.pack(fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.center_window()
        
        self.frames = {}
        
        for F in (StartPage, ComputerPage, UserListPage):
            page_name=F.__name__
            frame=F(parent=container, controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0, column=0, sticky=N+E+W+S)
            
        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        frame=self.frames[page_name]
        frame.tkraise()      
        
    def center_window(self):
        w=400
        h=600
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