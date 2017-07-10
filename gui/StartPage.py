'''
Created on 9 juil. 2017

@author: Gregory
'''
from tkinter import Frame, Button, ttk
from tkinter.constants import TOP, BOTH, X, HORIZONTAL

class StartPage(Frame):
    '''
    Home Frame
    '''
    def __init__(self, parent, controller):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.controller=controller
        
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(rowspan=1)
        separator.pack(side=TOP,fill=X)
        
        computerButton = Button(self, text="Computer Informations", command=lambda:controller.show_frame("ComputerPage"))
        computerButton.pack(side=TOP, fill=BOTH)
        
        userButton = Button(self, text="User Informations", command=lambda:controller.show_frame("UserListPage"))
        userButton.pack(side=TOP, fill=BOTH)