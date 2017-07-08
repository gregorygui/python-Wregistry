'''
Created on 6 juil. 2017

@author: Gregory
'''
import winreg

def read_subKeysNames(key, index, l):
    try:
        l.append(winreg.EnumKey(key, index))
        read_subKeysNames(key, index+1, l)
    finally:
        return l
    
def read_subKeysValues(key, index, l):
    try:
        l.append((winreg.EnumValue(key, index))[0])
        read_subKeysValues(key, index+1, l)
    finally:
        return l

def get_Users_HkeyUsers():
        return read_subKeysNames(winreg.HKEY_USERS, 0, [])
    
def get_Users_Hklm():
    key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList")
    return read_subKeysNames(key, 0, [])

class RegistryInspection:
    '''
    Gather informations from windows registry
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def get_Users(self):
        ul = get_Users_HkeyUsers()
        
        for u in get_Users_Hklm():
            if u not in ul:
                ul.append(u)
                
        return ul
    
    def get_Admins(self):
        ul = []
        
        for u in self.get_Users():
            if self.isAdmin(u):
                ul.append(u)
                
        return ul
    
    def isAdmin(self, sid):
        tmp=sid.split('-')
        if '500' in tmp[-1]:
            return True
        else:
            return False
    
    def get_LocalAccount(self):
        ul=[]
        
        for u in self.get_Users():
            if self.isLocal(u):
                ul.append(u)
                
        return ul
    
    def isLocal(self, sid):
        if 'S-1-5-21-12' in sid:
            return True
        else:
            return False
    
    def get_NetAccount(self):
        ul=[]
        
        for u in self.get_Users():
            if self.isNet(u):
                ul.append(u)
                
        return ul
    
    def isNet(self, sid):
        if 'S-1-5-21-13' in sid:
            return True
        else:
            return False
    
    def get_ProfilePath(self, sid):
        key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\" + sid)
        return (winreg.EnumValue(key, 0))[1]
    
    def get_ComputerName(self):
        key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName")
        return (winreg.EnumValue(key, 1))[1]
    
    def get_Run_Machine(self):
        key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
        key2=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce")
        return read_subKeysValues(key2, 0, read_subKeysValues(key, 0, read_subKeysNames(key, 0, [])))
    
    def get_Run_User(self, sid):
        key=winreg.OpenKey(winreg.HKEY_USERS, sid + "\Software\Microsoft\Windows\CurrentVersion\Run")
        key2=winreg.OpenKey(winreg.HKEY_USERS, sid + "\Software\Microsoft\Windows\CurrentVersion\RunOnce")
        return read_subKeysValues(key2, 0, read_subKeysValues(key, 0, read_subKeysNames(key, 0, [])))