from time import time
from dataclasses import dataclass
from .exceptions import MacAddressDoesNotExist
from templates.yang_py import sw_interface


@dataclass
class MacTableEntry:
    port: sw_interface.interface().interfaces.interface_entry
    timer: int
    last_seen: int


class MacTable:
    def __init__(self, max_age: int = 10) -> None:
        self.__max_age = max_age
        self.__entries: dict[str, MacTableEntry] = {}

    @property
    def max_age(self) -> int:
        return self.__max_age

    @max_age.setter
    def max_age(self, max_age: int) -> None:
        self.__max_age = max_age

    @property
    def entries(self) -> dict[str, MacTableEntry]:
        return self.__entries
    
    def add_entry(self, mac_address: str, port: sw_interface.interface().interfaces.interface_entry) -> None:
        self.__entries[mac_address] = MacTableEntry(port, self.__max_age, time())

    def remove_entry(self, mac_address: str) -> None:
        try:
            del self.__entries[mac_address]
        except KeyError:
            raise MacAddressDoesNotExist
        
    def update(self) -> None:
        rm_list = []
        for mac_address, entry in self.__entries.items():
            if time() - entry.last_seen > entry.timer:
                rm_list.append(mac_address)
        for mac_address in rm_list:
            self.remove_entry(mac_address)
        
    def statistics(self) -> dict[str, int]:
        return {
            "entries": len(self.__entries),
            "max_age": self.__max_age
        }
    
