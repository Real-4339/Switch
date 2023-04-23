import asyncio
import json

from app.di.core import core


class WebsocketContainer:
    def __init__(self) -> None:
        self.__clients = set()
        self.__mac_table = None
        self.__loop = core.loop

    @property
    def clients(self) -> set:
        return self.__clients
    
    @property
    def mac_table(self) -> dict:
        return self.__mac_table
    
    @mac_table.setter
    def mac_table(self, mac_table: dict) -> None:
        self.__mac_table = mac_table
        self.__loop.create_task(self.__update_mac_table())

    # async def __run(self) -> None:
    #     self.__loop.create_task(self.__update_mac_table())

    async def __update_mac_table(self) -> None:
        data = {"type": "updateMacTable", "macTable": list(self.__mac_table)}
        json_data = json.dumps(data)

        for client in self.__clients:
            await client.send_text(json_data)
    

    # self.__loop.run_until_complete(self.__run())
    