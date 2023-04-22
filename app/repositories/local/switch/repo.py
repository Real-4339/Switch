from app.di.sources import sources 
from .model import Switch, Interface

class LocalSwitchRepo:
    def __init__(self):
        self.local_switch = sources.local_switch

    def create(self):
        '''Boot a switch'''
        self.local_switch.boot()

    def get(self):
        '''Get all statistics'''
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def delete(self):
        '''Shutdown a switch'''
        raise NotImplementedError
    

class InterfaceRepo:
    def __init__(self):
        self.local_switch = sources.local_switch
        self.local_interface = sources.local_switch_interface

    def create(self):
        '''Is boot with switch'''
        raise NotImplementedError

    def get(self):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def delete(self):
        raise NotImplementedError
    

class MacRepo:
    def __init__(self):
        self.local_switch = sources.local_switch
        self.local_mac = sources.local_switch_mac

    def create(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def delete(self):
        raise NotImplementedError