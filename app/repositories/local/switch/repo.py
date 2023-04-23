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

    def get(self, command: str = None):
        '''Get all statistics or name of switch'''
        if command == 'name':
            return self.local_switch.name

    def update(self, command: str, interfaces: list = None, name: str = None):
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
                self.local_switch.delete_inter_to_run(interface)
        elif command == 'name':
            self.local_switch.name = name
            return self.local_switch.name
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

    def get(self, command: str = None, interface: str = None):
        '''Get all interfaces or a specific interface'''
        if command == 'get interface':
            return self.local_switch.interface_manager.get_interface(interface)
        elif command == 'all':
            return self.local_switch.interface_manager.get_interfaces()
        elif command == 'up':
            return self.local_switch.working_interfaces.keys() if self.local_switch.running else {}
        elif command == 'down':
            return self.local_switch.interface_manager.get_keys() - self.local_switch.working_interfaces.keys() if self.local_switch.running else self.local_switch.interface_manager.get_keys()
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
        '''Get timer'''
        return self.local_mac.max_age
    
    def update(self, timer: int = None):
        '''Update macs time to live'''
        self.local_mac.update_timer(timer)
        return self.local_mac.max_age
    
    def delete(self):
        '''Delete all macs'''
        self.local_mac.remove_all()