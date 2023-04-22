import logging

from app.di.sources import sources 


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# Create a StreamHandler and set its level to INFO
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
log.addHandler(handler)


class LocalSwitchRepo:
    def __init__(self):
        self.local_switch = sources.local_switch

    def create(self):
        '''Boot a switch'''
        self.local_switch.boot()

    def get(self):
        '''Get all statistics'''
        raise NotImplementedError
    
    def update(self, command: str, interfaces: list = None):
        '''Run, Stop, Reset a switch'''
        if command == 'run':
            try:
                self.local_switch.run()
            except:
                log.error('Switch is already running')
        elif command == 'stop':
            try:
                self.local_switch.stop()
            except:
                log.error('Switch is already stopped')
        elif command == 'add interface':
            for interface in interfaces:
                self.local_switch.choose_inter_to_run(interface)
        elif command == 'delete interface':
            for interface in interfaces:
                self.local_switch.choose_inter_to_stop(interface)
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
    
    def update(self, command: str, interfaces: list = None):
        '''Update interface name or state, or both, or even add a new interface'''
        if command == 'add interface':
            for interface in interfaces:
                self.local_switch.interface_manager.add_interface(interface)
        elif command == 'delete interface':
            for interface in interfaces:
                self.local_switch.interface_manager.remove_interface(interface)
    
    def delete(self):
        raise NotImplementedError
    

class MacRepo:
    def __init__(self):
        self.local_switch = sources.local_switch
        self.local_mac = sources.local_switch_mac

    def create(self):
        '''Created with switch'''
        raise NotImplementedError

    def get(self):
        '''Get all macs'''
        raise NotImplementedError
    
    def update(self):
        '''Update macs time to live'''
        raise NotImplementedError
    
    def delete(self):
        '''Delete all macs'''
        raise NotImplementedError