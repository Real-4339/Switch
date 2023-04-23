import asyncio
import json


class WebsocketContainer:
    def __init__(self) -> None:
        self.__clients = set()
        self.__mac_table = None
        self.__loop = asyncio.new_event_loop()

    @property
    def clients(self) -> set:
        return self.__clients
    
    @property
    def mac_table(self) -> dict:
        return self.__mac_table
    
    @mac_table.setter
    def mac_table(self, mac_table: dict) -> None:
        self.__mac_table = mac_table
        self.__loop.run_until_complete(self.__run(mac_table))

    async def __run(self, mac_table: dict) -> None:
        self.__loop.create_task(self.__update_mac_table(mac_table))

    async def __update_mac_table(self, mac_table: dict) -> None:
        data = {"type": "updateMacTable", "macTable": list(mac_table)}
        json_data = json.dumps(data)
        
        print("Sending data to clients")

        for client in self.__clients:
            await client.send_text(json_data)
    