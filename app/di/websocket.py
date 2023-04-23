from typing import Callable
from functools import cached_property


class WebsocketContainer:
    '''
    Websocket container
    I call functions from this class from mac-table and switch to send data to frontend
    broadcast_mac_table - are called from mac-table setter, which already contains websocket function to send data to frontend,
    it contains callable function from websocket.py
    '''
    def __init__(self) -> None:
        self.__clients = set()
        self.__mac_table = None

    @property
    def clients(self) -> set:
        return self.__clients
    
    @property
    def mac_table(self) -> dict:
        return self.__mac_table
    
    @mac_table.setter
    def mac_table(self, mac_table: dict) -> None:
        self.__mac_table = mac_table
        self.call_mac_update(mac_table)
        

    def set_mac_update(self, mac_update: Callable) -> None:
        self.__mac_update = mac_update

    async def call_mac_update(self, mac_table: dict) -> None:
        await self.__mac_update(mac_table)