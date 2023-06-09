from typing import Callable
from scapy.all import AsyncSniffer, Packet
from .exceptions import SnifferIsActive
from .switch import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# Create a StreamHandler and set its level to INFO
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
log.addHandler(handler)


class Sniffer:
    def __init__(self, inerface: str, handler: Callable[[str, Packet], None] = None) -> None:
        self.__interface = inerface
        self.__running = False
        self.__sniffer = AsyncSniffer(iface=inerface, prn=self.__handlePacket, store=False)
        self.__packet_handler = handler

    @property
    def running(self) -> bool:
        return self.__running
    
    @property
    def interface(self) -> str:
        return self.__interface
    
    def __handlePacket(self, packet: Packet) -> None:
        if self.__packet_handler is not None:
            self.__packet_handler(self.__interface, packet)

    def start(self) -> None:
        if self.__running:
            raise SnifferIsActive
        log.info('Starting sniffer on interface: %s', self.__interface)
        self.__running = True
        self.__sniffer.start()

    def stop(self) -> None:
        self.__running = False
        self.__sniffer.stop()
        log.info('Stopping sniffer on interface: %s', self.__interface)
        self.__packet_handler = None