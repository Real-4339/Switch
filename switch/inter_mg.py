import psutil
import pyangbind.lib.pybindJSON as pybindJSON

from typing import OrderedDict
from templates.yang_py import sw_interface
from exceptions import InterfaceDoesNotExist, InvalidState


class InterfaceManager:
    def __init__(self):
        self.__interface_container = sw_interface.interface().interfaces

    def boot(self) -> None:
        for interface in psutil.net_if_addrs():
            new_interface = self.__interface_container.interface_entry.add(interface)
            new_interface.state = "down"

    def add_interface(self, interface_name: str) -> None:
        new_interface = self.__interface_container.interface_entry.add(interface_name)
        new_interface.state = "down"

    def remove_interface(self, interface_name: str) -> None:
        try:
            self.__interface_container.interface_entry.remove(interface_name)
        except AttributeError:
            raise InterfaceDoesNotExist
        
    def get_interface(self, interface_name: str) -> OrderedDict:
        try:
            return self.__interface_container.interface_entry[interface_name]
        except AttributeError:
            raise InterfaceDoesNotExist

    def get_interfaces(self):
        return self.__interface_container
    
    def update_interface_name(self, old_name: str, new_name: str) -> None:
        if old_name not in self.__interface_container.interface_entry:
            raise InterfaceDoesNotExist
        self.__interface_container.interface_entry.remove(old_name)
        new_interface = self.__interface_container.interface_entry.add(new_name)
        new_interface.state = "down"

    def update_interface_state(self, interface_name: str, state: str) -> None:
        if state not in ["up", "down"]:
            raise InvalidState
        if interface_name not in self.__interface_container.interface_entry:
            raise InterfaceDoesNotExist
        self.__interface_container.interface_entry[interface_name].state = state

    def return_json(self) -> OrderedDict:
        return pybindJSON.dumps(self.__interface_container)
    
    def return_interface_json(self, interface_name: str) -> OrderedDict:
        if interface_name not in self.__interface_container.interface_entry:
            raise InterfaceDoesNotExist
        return pybindJSON.dumps(self.__interface_container.interface_entry[interface_name])