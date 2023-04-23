from __future__ import annotations
import logging
import app.di.containers as di_containers



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
    def __init__(self, containers: di_containers.Containers):
        self.__containers = containers

    def create(self):
        '''Boot a switch'''
        self.__containers.sources.local_switch.boot()

    def get(self, command: str | None = None):
        '''Get all statistics or name of switch'''
        if command == 'name':
            return self.__containers.sources.local_switch.name

    def update(self, command: str, interfaces: list | None = None, name: str | None = None):
        '''Run, Stop, Reset a switch'''
        if command == 'run':
            try:
                self.__containers.sources.local_switch.run()
            except:
                log.error('Switch is already running')
        elif command == 'stop':
            try:
                self.__containers.sources.local_switch.stop()
            except:
                log.error('Switch is already stopped')
        elif command == 'add interface' and interfaces:
            for interface in interfaces:
                self.__containers.sources.local_switch.choose_inter_to_run(interface)
        elif command == 'delete interface' and interfaces:
            for interface in interfaces:
                self.__containers.sources.local_switch.delete_inter_to_run(interface)
        elif command == 'name' and name:
            self.__containers.sources.local_switch.name = name
            return self.__containers.sources.local_switch.name
        else:
            raise NotImplementedError
    
    def delete(self):
        '''Shutdown a switch'''
        try:
            self.__containers.sources.local_switch.stop()
        finally:
            self.__containers.sources.local_switch.shutdown()


class InterfaceRepo:
    def __init__(self, containers: di_containers.Containers):
        self.__containers = containers

    def create(self):
        '''Is booted with switch'''
        raise NotImplementedError

    def get(self, command: str | None = None, interface: str | None = None):
        '''Get all interfaces or a specific interface'''
        if command == 'get interface' and interface:
            return self.__containers.sources.local_switch.interface_manager.get_interface(interface)
        elif command == 'all':
            return self.__containers.sources.local_switch.interface_manager.get_interfaces()
        elif command == 'up':
            return self.__containers.sources.local_switch.working_interfaces.keys() if self.__containers.sources.local_switch.running else {}
        elif command == 'down':
            return self.__containers.sources.local_switch.interface_manager.get_keys() - self.__containers.sources.local_switch.working_interfaces.keys() if self.__containers.sources.local_switch.running else self.__containers.sources.local_switch.interface_manager.get_keys()
        else:
            return self.__containers.sources.local_switch.interface_manager.get_keys()
    
    def update(self, command: str, interfaces: list | None = None, interface: str | None = None, state: str | None = None):
        '''Update interface name or state, or both, or even add a new interface'''
        if command == 'add interface' and interfaces:
            for interface_ in interfaces:
                self.__containers.sources.local_switch.interface_manager.add_interface(interface_)
        elif command == 'update state':
            if interface in self.__containers.sources.local_switch.working_interfaces:
                if state == 'up':
                    return {'error': 'Interface is already up'}
                elif state == 'down':
                    self.__containers.sources.local_switch.stop_working_interface(interface)
            else:
                if not self.__containers.sources.local_switch.booted or not interface or not state:
                    return {'error': 'Switch is not booted'}
                self.__containers.sources.local_switch.interface_manager.update_interface_state(interface, state)
                return {'name': interface, 'new state': state}
                
        elif command == 'delete interface' and interfaces:
            for interface_ in interfaces:
                self.__containers.sources.local_switch.interface_manager.remove_interface(interface_)
    
    def delete(self):
        raise NotImplementedError
    

class MacRepo:
    def __init__(self, containers: di_containers.Containers):
        self.__containers = containers

    def create(self):
        '''Created with switch'''
        raise NotImplementedError

    def get(self):
        '''Get timer'''
        return self.__containers.sources.local_switch.mac_table.max_age
    
    def update(self, timer: int | None = None):
        '''Update macs time to live'''
        self.__containers.sources.local_switch.mac_table.update_timer(timer or 0)
        return self.__containers.sources.local_switch.mac_table.max_age
    
    def delete(self):
        '''Delete all macs'''
        self.__containers.sources.local_switch.mac_table.remove_all()