'''
Created on 5 juil. 2017

@author: Gregory
'''
from gui import launch_gui

def userSummary(regI):
    us=regI.get_Admins()
    if(len(us)>0):
        print(str(len(us))+" admin(s) found:")
        for a in us:
            print("\t"+a)
            
    us=regI.get_LocalAccount()
    if(len(us)>0):
        print(str(len(us))+" local user(s) found:")
        for a in us:
            print("\t"+a)
            
    us=regI.get_NetAccount()
    if(len(us)>0):
        print(str(len(us))+" network user(s) found:")
        for a in us:
            print("\t"+a)

def main():
    launch_gui()

if __name__ == '__main__':
    main()