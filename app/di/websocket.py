import asyncio
import json


class WebsocketContainer:
    def __init__(self, core) -> None:
        self.__clients = set()
        self.__mac_table = None
        self.__port1_statistic: list[dict[str, list]]
        self.__port2_statistic: list[dict[str, list]]
        self.__loop = core.loop

    @property
    def clients(self) -> set:
        return self.__clients
    
    @property
    def port1_statistic(self) -> list[dict[str, list]]:
        return self.__port1_statistic
    
    @property
    def port2_statistic(self) -> list[dict[str, list]]:
        return self.__port2_statistic

    @property
    def mac_table(self) -> dict:
        return self.__mac_table
    
    @mac_table.setter
    def mac_table(self, mac_table: dict) -> None:
        self.__mac_table = mac_table
        self.__loop.create_task(self.__update_mac_table())
    
    @port1_statistic.setter
    def port1_statistic(self, port1_statistic: list[dict[str, list]]) -> None:
        self.__port1_statistic = port1_statistic
        self.__loop.create_task(self.__update_statistic1())

    @port2_statistic.setter
    def port2_statistic(self, port2_statistic: list[dict[str, list]]) -> None:
        self.__port2_statistic = port2_statistic
        self.__loop.create_task(self.__update_statistic2())

    def add_log(self, log: str) -> None:
        self.__loop.create_task(self.__push_log(log))
    
    async def __push_log(self, log: str) -> None:
        data = {"type": "log", "log": log}
        json_data = json.dumps(data)

        for client in self.__clients:
            await client.send_text(json_data)

    async def __update_mac_table(self) -> None:
        data = {"type": "updateMacTable", "macTable": list(self.__mac_table)}
        json_data = json.dumps(data)

        for client in self.__clients:
            await client.send_text(json_data)

    async def __update_statistic1(self) -> None:
        data = {"type": "updatePort", "port": "port1", "list": self.__port1_statistic}
        json_data = json.dumps(data)

        for client in self.__clients:
            await client.send_text(json_data)

    async def __update_statistic2(self) -> None:
        data = {"type": "updatePort", "port": "port2", "list": self.__port2_statistic}
        json_data = json.dumps(data)

        for client in self.__clients:
            await client.send_text(json_data)


    # async def __run(self) -> None:
    #     self.__loop.create_task(self.__update_mac_table())

    # self.__loop.run_until_complete(self.__run())
    