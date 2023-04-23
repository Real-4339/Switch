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
        pass

    def create(self):
        '''Boot a switch'''
        sources.local_switch.boot()

    def get(self, command: str = None):
        '''Get all statistics or name of switch'''
        if command == 'name':
            return sources.local_switch.name

    def update(self, command: str, interfaces: list = None, name: str = None):
        '''Run, Stop, Reset a switch'''
        if command == 'run':
            try:
                sources.local_switch.run()
            except:
                log.error('Switch is already running')
        elif command == 'stop':
            try:
                sources.local_switch.stop()
            except:
                log.error('Switch is already stopped')
        elif command == 'add interface':
            for interface in interfaces:
                sources.local_switch.choose_inter_to_run(interface)
        elif command == 'delete interface':
            for interface in interfaces:
                sources.local_switch.delete_inter_to_run(interface)
        elif command == 'name':
            sources.local_switch.name = name
            return sources.local_switch.name
        else:
            raise NotImplementedError
    
    def delete(self):
        '''Shutdown a switch'''
        try:
            sources.local_switch.stop()
        finally:
            sources.local_switch.shutdown()


class InterfaceRepo:
    def __init__(self):
        pass

    def create(self):
        '''Is booted with switch'''
        raise NotImplementedError

    def get(self, command: str = None, interface: str = None):
        '''Get all interfaces or a specific interface'''
        if command == 'get interface':
            return sources.local_switch.interface_manager.get_interface(interface)
        elif command == 'all':
            return sources.local_switch.interface_manager.get_interfaces()
        elif command == 'up':
            return sources.local_switch.working_interfaces.keys() if sources.local_switch.running else {}
        elif command == 'down':
            return sources.local_switch.interface_manager.get_keys() - sources.local_switch.working_interfaces.keys() if sources.local_switch.running else sources.local_switch.interface_manager.get_keys()
        else:
            return sources.local_switch.interface_manager.get_keys()
    
    def update(self, command: str, interfaces: list = None, interface: str = None, state: str = None):
        '''Update interface name or state, or both, or even add a new interface'''
        if command == 'add interface':
            for interface in interfaces:
                sources.local_switch.interface_manager.add_interface(interface)
        elif command == 'update state':
            if interface in sources.local_switch.working_interfaces:
                if state == 'up':
                    return {'error': 'Interface is already up'}
                elif state == 'down':
                    sources.local_switch.stop_working_interface(interface)
            else:
                if not sources.local_switch.booted:
                    return {'error': 'Switch is not booted'}
                sources.local_switch.interface_manager.update_interface_state(interface, state)
                return {'name': interface, 'new state': state}
                
        elif command == 'delete interface':
            for interface in interfaces:
                sources.local_switch.interface_manager.remove_interface(interface)
    
    def delete(self):
        raise NotImplementedError
    

class MacRepo:
    def __init__(self):
        pass

    def create(self):
        '''Created with switch'''
        raise NotImplementedError

    def get(self):
        '''Get timer'''
        return sources.local_switch.mac_table.max_age
    
    def update(self, timer: int = None):
        '''Update macs time to live'''
        sources.local_switch.mac_table.update_timer(timer)
        return sources.local_switch.mac_table.max_age
    
    def delete(self):
        '''Delete all macs'''
        sources.local_switch.mac_table.remove_all()