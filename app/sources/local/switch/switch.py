import logging

from .mac import MacTable
from .console import Console
from .sniffer import Sniffer
from app.di import containers
from scapy.packet import Packet
from scapy.sendrecv import sendp
from scapy.layers.l2 import Ether
from .inter_mg import InterfaceManager
from .exceptions import SwitchIsActive, SwitchIsNotActive, InterfaceDoesNotExist


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


class Switch:
    __version__ = '3.0.1'
    
    def __init__(self) -> None:
        self.__running = False
        self.__mac_table = MacTable()
        self.__console = Console(self)
        self.__interface_manager = InterfaceManager()
        self.__working_interfaces: dict[str, Sniffer] = {}

    @property
    def running(self) -> bool:
        return self.__running
    
    @property
    def interface_manager(self) -> InterfaceManager:
        return self.__interface_manager
    
    @property
    def mac_table(self) -> MacTable:
        return self.__mac_table
    
    @property
    def console(self) -> Console:
        return self.__console
    
    @property
    def working_interfaces(self) -> dict[str, Sniffer]:
        return self.__working_interfaces
    
    def __send_packet(self, packet: Packet, inter_from: str) -> None:
        
        if packet[Ether].dst in self.__mac_table.entries:
            interface = self.__mac_table.entries[packet[Ether].dst].port.name
            sendp(packet, iface=interface, verbose=False)
        else:
            for interface in self.__working_interfaces:
                if interface != inter_from:
                    sendp(packet, iface=interface, verbose=False)

        log.info(f'Packet to {interface} is sent')

    def __packet_handler(self, interface: str, packet: Packet) -> None:
        log.info(f'Packet from {interface} is received')
        
        if not packet.getlayer(Ether): 
            log.info('Packet is not Ethernet')
            return
        
        inter = self.__interface_manager.get_interface(interface)
        
        len_before = len(self.__mac_table.entries)

        self.__mac_table.add_or_update_entry(packet[Ether].src, inter)
        self.__mac_table.update()

        if len(self.__mac_table.entries) != len_before:
            containers.websocket.mac_table = self.__mac_table.entries

        # self.__send_packet(packet, interface)

    def boot(self) -> None:
        if self.__running:
            raise SwitchIsActive
        self.__interface_manager.boot()
        log.info('Switch is active')

    def choose_inter_to_run(self, interface_name: str) -> None:
        if self.__running:
            raise SwitchIsActive
        if interface_name not in self.__interface_manager.get_keys():
            raise InterfaceDoesNotExist
        self.__working_interfaces[interface_name] = Sniffer(interface_name, self.__packet_handler)
        log.info(f'Interface {interface_name} is added to working interfaces')

    def delete_inter_to_run(self, interface_name: str) -> None:
        if self.__running:
            raise SwitchIsActive
        del self.__working_interfaces[interface_name]

    def run(self) -> None:
        if self.__running:
            raise SwitchIsActive
        self.__running = True
        for interface in self.__working_interfaces.values():
            interface.start()
        log.info('Switch is running')

    def stop(self) -> None:
        if not self.__running:
            raise SwitchIsNotActive
        for interface in self.__working_interfaces.values():
            interface.stop()
        self.__running = False
        log.info('Switch is stopped')

    def shutdown(self) -> None:
        if self.__running:
            raise SwitchIsActive
        self.__interface_manager.shutdown()
        log.info('Switch is shutdown')
