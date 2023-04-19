from scapy.all import AsyncSniffer, Packet


class Sniffer:
    def __init__(self, inerface: str):
        self.__interface = inerface
        self.__running = False
        self.__sniffer = AsyncSniffer()