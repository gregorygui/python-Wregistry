'''
Created on 9 juil. 2017

@author: Gregory
'''
from tkinter import Frame, Button

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
        
        computerButton = Button(self, text="Computer Informations", command=lambda:controller.show_frame("ComputerPage"))
        computerButton.pack(side="top", fill="x", expand=True)
        
        userButton = Button(self, text="User Informations", command=lambda:controller.show_frame("UserPage"))
        userButton.pack(side="bottom", fill="both", expand=True)