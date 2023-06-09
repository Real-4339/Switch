import threading

from time import time
from .inter_mg import pybindJSON
from dataclasses import dataclass
from .exceptions import MacAddressDoesNotExist
from app.presentation.resources.templates.yang_py import sw_interface


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
        with threading.Lock():
            self.__max_age = max_age

    @property
    def entries(self) -> dict[str, MacTableEntry]:
        return self.__entries.copy()
    
    def add_or_update_entry(self, mac_address: str, port: sw_interface.interface().interfaces.interface_entry) -> None:
        with threading.Lock():
            self.__entries[mac_address] = MacTableEntry(port, self.__max_age, time())

    def remove_entry(self, mac_address: str) -> None:
        try:
            with threading.Lock():
                del self.__entries[mac_address]
        except KeyError:
            raise MacAddressDoesNotExist
        
    def update(self) -> bool:
        rm_list = []
        with threading.Lock():
            for mac_address, entry in self.__entries.items():
                if time() - entry.last_seen > entry.timer:
                    rm_list.append(mac_address)
            
            for mac_address in rm_list:
                self.remove_entry(mac_address)

    def remove_all(self) -> None:
        with threading.Lock():
            self.__entries.clear()

    def update_timer(self, timer: int) -> None:
        self.max_age = timer
        with threading.Lock():
            for entry in self.__entries.values():
                entry.timer = timer
        
    def statistics(self) -> dict[str, int]:
        return {
            "entries": len(self.__entries),
            "max_age": self.__max_age
        }
    
    def dump_json(self) -> str:
        return pybindJSON.dumps(self.__entries)
    
