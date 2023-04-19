import time as time

from templates.yang_py import sw_mac_table
from templates.yang_py import sw_interface

class MacTableManager:
    def __init__(self):
        self.__mac_table_container = sw_mac_table.mac_table()

    def add_mac_table_entry(self, mac_address: str, interface_name: sw_interface.interface.interfaces) -> None:
        new_mac_table_entry = self.__mac_table_container.mac.add(mac_address)
        new_mac_table_entry.timer = 10
        new_mac_table_entry.port = interface_name
