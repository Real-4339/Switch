from app.repositories.local.switch.model import Switch, Interface, MacTable, MacTableEntry
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
    def mac_table_entry(self) -> MacTableEntry:
        return MacTableEntry
