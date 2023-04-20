import logging

from inter_mg import InterfaceManager
from mac import MacTable
from exceptions import SwitchIsActive

class Switch:
    __version__ = '3.0.1'

    def __init__(self) -> None:
        self.__running = False
        self.__interface_manager = InterfaceManager()
        self.__mac_table = MacTable()
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
    
    def boot(self) -> None:
        if self.__running:
            raise SwitchIsActive
        self.__running = True
        self.logger.info('Switch is active')