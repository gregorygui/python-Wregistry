'''
Created on 6 juil. 2017

@author: Gregory
'''

class User(object):
    '''
    Class to store User informations discovery
    '''

    def __init__(self, sid, ipp):
        '''
        Constructor
        '''
        self.sid = sid
        self.type = 'Local'
        self.isAdmin = False
        self.ipp = ipp
        self.run = []
        
        if "DEFAULT" in self.sid:
            self.name='Default'
        elif "S-1-5-18" in self.sid:
            self.name='LocalSystem'
        elif "S-1-5-19" in self.sid:
            self.name='LocalService'
        elif "S-1-5-20" in self.sid:
            self.name='NetworkService'
        else:
            self.name=((self.ipp).split('\\'))[-1]
        
    def get_sid(self):
        return self.sid
    
    def set_sid(self, sid):
        self.sid=sid
        
    def get_isAdmin(self):
        return self.isAdmin
    
    def set_Admin(self):
        self.isAdmin=True
        
    def get_ipp(self):
        return self.ipp
    
    def set_ipp(self, ipp):
        self.ipp=ipp
        
    def get_type(self):
        return self.type
    
    def set_type_local(self):
        self.type='Local'
        
    def set_type_net(self):
        self.type='Net'
        
    def get_run(self):
        return self.run
    
    def add_run(self, v):
        self.run.append(v)
        
    def set_run(self, l):
        self.run=l
        
    def get_name(self):
        return self.name
    
    def set_name(self, n):
        self.name=n