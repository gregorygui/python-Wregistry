'''
Created on 6 juil. 2017

@author: Gregory
'''
from tools.RegistryInspection import RegistryInspection

class UserList(object):
    '''
    Class to store All Users
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.regi = RegistryInspection()
        self.ulist = []
        self.build_list()
            
    def build_list(self):
        self.ulist = []
        
        for sid in self.regi.get_Users():

            u = User(sid, self.regi.get_ProfilePath(sid))
            
            if not u.get_name():
                continue
           
            if self.regi.isAdmin(u.sid):
                u.set_Admin()
                
            if self.regi.isNet(u.sid):
                u.set_type_net()
                
            u.set_run(self.regi.get_Run_User(sid))
            
            self.ulist.append(u)
        
        sorted(self.ulist, key=lambda user: user.name)
            
    def get_list(self):
        return self.ulist
    
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
            try:
                self.name=(self.ipp.split('\\'))[-1]
            except:
                self.name=None
        
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