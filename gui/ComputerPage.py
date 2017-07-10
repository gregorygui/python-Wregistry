'''
Created on 9 juil. 2017

@author: Gregory
'''
from tkinter import Frame, Label, Listbox
from tools.Machine import Machine
from tkinter.constants import X, LEFT, TOP, END

class ComputerPage(Frame):
    '''
    Frame with computer informations
    '''


    def __init__(self, parent, controller):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.controller = controller
        self.computer = Machine()
        
        computerName = Label(self, text="Computer Name = "+self.computer.name)
        computerName.pack(fill=X, side=TOP)
        
        run = self.computer.get_run()
        
        runLabel = Label(self, text=str(len(run))+ " Run/RunOnce service(s) found")
        runLabel.pack(fill=X, side=LEFT)
        
        listbox = Listbox(self)
        
        for s in run:
            listbox.insert(END, s)
            
        listbox.pack(fill=X, side=LEFT)