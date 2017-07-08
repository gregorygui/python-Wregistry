'''
Created on 9 juil. 2017

@author: Gregory
'''
from tkinter import Frame, Label
from tools import RegistryInspection

class ComputerPage(Frame):
    '''
    Frame with computer informations
    '''


    def __init__(self, parent, controller):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.controller=controller
        self.inspection = RegistryInspection.RegistryInspection()
        
        computerName = Label(self, text="Computer Name = "+self.inspection.get_ComputerName())
        computerName.pack()