from switch.inter_mg import InterfaceManager
from exceptions import InterfaceDoesNotExist, InvalidState, SwitchIsActive, SwitchIsNotActive

class Switch:
    __version__ = '3.0.1'

    def __init__(self) -> None:
        self.__running = False
        self.__interface_manager = InterfaceManager()