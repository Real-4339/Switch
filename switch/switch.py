import logging

from mac import MacTable
from sniffer import Sniffer
from scapy.packet import Packet
from inter_mg import InterfaceManager
from exceptions import SwitchIsActive, SwitchIsNotActive



class Switch:
    __version__ = '3.0.1'

    def __init__(self) -> None:
        self.__running = False
        self.__mac_table = MacTable()
        self.__interface_manager = InterfaceManager()
        self.__working_interfaces = dict[str, Sniffer] = {}
        self.logger = self.__setLogger('DEBUG')

    @property
    def running(self) -> bool:
        return self.__running
    
    @property
    def logger(self) -> logging.Logger:
        return self.__logger
    
    @property
    def interface_manager(self) -> InterfaceManager:
        return self.__interface_manager
    
    @property
    def mac_table(self) -> MacTable:
        return self.__mac_table
    
    @logger.setter
    def logger(self, logger_lvl: str) -> None:
        self.__logger.setLevel(logger_lvl)

    def __setLogger(self, logger_lvl: str) -> logging.Logger:
        logger = logging.getLogger(__name__)
        logger.setLevel(logger_lvl)
        return logger
    
    def __packet_handler(self, interface: str, packet: Packet) -> None:
        self.logger.info(f'Packet from {interface} is received')
        ...

    def boot(self) -> None:
        if self.__running:
            raise SwitchIsActive
        self.__running = True
        self.__interface_manager.boot()
        self.logger.info('Switch is active')

    def choose_inter_to_run(self, interface_name: str) -> None:
        if self.__running:
            raise SwitchIsActive
        self.__working_interfaces[interface_name] = Sniffer(interface_name, self.__packet_handler)

    def delete_inter_to_run(self, interface_name: str) -> None:
        if self.__running:
            raise SwitchIsActive
        del self.__working_interfaces[interface_name]

    def run(self) -> None:
        if not self.__running:
            raise SwitchIsNotActive
        for interface in self.__working_interfaces.values():
            interface.start()
        self.logger.info('Switch is running')

    def stop(self) -> None:
        if not self.__running:
            raise SwitchIsNotActive
        for interface in self.__working_interfaces.values():
            interface.stop()
        self.logger.info('Switch is stopped')

    def shutdown(self) -> None:
        if not self.__running:
            raise SwitchIsNotActive
        self.__running = False
        self.__interface_manager.shutdown()
        self.logger.info('Switch is shutdown')
