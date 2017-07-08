'''
Created on 6 juil. 2017

@author: Gregory
'''

class Machine(object):
    '''
    Store computer informations
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
        self.run=[]
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