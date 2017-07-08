'''
Created on 9 juil. 2017

@author: Gregory
'''
from tkinter import Frame

class UserPage(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent, controller):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.controller=controller