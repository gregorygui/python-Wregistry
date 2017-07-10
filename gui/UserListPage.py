'''
Created on 9 juil. 2017

@author: Gregory
'''
from tkinter import Frame, Button
from tools.User import UserList
from tkinter.constants import TOP, X

class UserListPage(Frame):
    '''
    Page for users informations
    '''

    def __init__(self, parent, controller):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.controller=controller
        self.ul = UserList()
        self.ul.build_list()
        
        for user in self.ul.get_list():
            l = Button(self, text=user.get_name())
            l.pack(side=TOP, expand=True, fill=X)