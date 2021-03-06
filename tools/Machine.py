'''
Created on 6 juil. 2017

@author: Gregory
'''
from tools.RegistryInspection import RegistryInspection

class Machine(object):
    '''
    Store computer informations
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.regi=RegistryInspection()
        self.name=self.regi.get_ComputerName()
        self.run=self.regi.get_Run_Machine()
        self.interfaces=[]
        
    def get_name(self):
        return self.name
    
    def set_name(self, n):
        self.name=n
        
    def get_run(self):
        return self.run
    
    def add_run(self, v):
        self.run.append(v)
        
    def set_run(self, l):
        self.run=l
        
    def get_interfaces(self):
        return self.interfaces
    
    def add_interface(self, v):
        self.interfaces.append(v)
        
    def set_interfaces(self, l):
        self.interfaces=l