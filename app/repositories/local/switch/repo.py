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
    
    def update(self, command: str):
        '''Run, Stop, Reset a switch'''
        if command == 'run':
            self.local_switch.run()
        elif command == 'stop':
            self.local_switch.stop()
        else:
            raise NotImplementedError
    
    def delete(self):
        '''Shutdown a switch'''
        try:
            self.local_switch.stop()
        finally:
            self.local_switch.shutdown()
    

class InterfaceRepo:
    def __init__(self):
        self.local_switch = sources.local_switch
        self.local_interface = sources.local_switch_interface

    def create(self):
        '''Is booted with switch'''
        raise NotImplementedError

    def get(self, command: str = None):
        '''Get all interfaces or a specific interface'''
        if command:
            return self.local_switch.interface_manager.get_interface(command)
        else:
            return self.local_switch.interface_manager.get_keys()
    
    def update(self, command: str, interface_name: str = None, state: str = None):
        '''Update interface name or state, or both, or even add a new interface'''
        raise NotImplementedError
    
    def delete(self):
        '''Delete an interface'''
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