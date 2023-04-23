from app.repositories.local.switch.model import (
    Switch, Interface, MacTable, LocalSwitch, InterfaceName
)
from functools import cached_property


class ModelContainer:
    @cached_property
    def switch(self) -> Switch:
        return Switch
    
    @cached_property
    def interface(self) -> Interface:
        return Interface
    
    @cached_property
    def mac_table(self) -> MacTable:
        return MacTable
    
    @cached_property
    def local_switch(self) -> LocalSwitch:
        return LocalSwitch
    
    @cached_property
    def interface_name(self) -> InterfaceName:
        return InterfaceName
