import logging

from .mac import MacTable
from .console import Console
from .sniffer import Sniffer
from scapy.packet import Packet
from scapy.sendrecv import sendp
from .inter_mg import InterfaceManager
from scapy.layers.l2 import Ether, ARP
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP, TCP, UDP, ICMP
from .exceptions import (SwitchIsActive, 
                         SwitchIsNotActive, 
                         InterfaceDoesNotExist)


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
    
    def __init__(self, containers) -> None:
        self.__name = 'Switch'
        self.__running = False
        self.__booted = False
        self.__sending = False
        self.__mac_table = MacTable()
        self.__console = Console(self)
        self.__interface_manager = InterfaceManager()
        self.__working_interfaces: dict[str, Sniffer] = {}
        self.__port1: str = None
        self.__port2: str = None
        self.__port1_statistic: list[dict[str, list]] = [{"value1": [], "value2": []}]
        self.__port2_statistic: list[dict[str, list]] = [{"value1": [], "value2": []}]
        self.__containers = containers
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def running(self) -> bool:
        return self.__running
    
    @property
    def booted(self) -> bool:
        return self.__booted
    
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
    
    @property
    def port1(self) -> str:
        return self.__port1
    
    @property
    def port2(self) -> str:
        return self.__port2
    
    @property
    def port1_statistic(self) -> list[dict[str, list]]:
        return self.__port1_statistic
    
    @property
    def port2_statistic(self) -> list[dict[str, list]]:
        return self.__port2_statistic
    
    @port1_statistic.setter
    def port1_statistic(self, port1_statistic: list[dict[str, list]]) -> None:
        self.__port1_statistic = port1_statistic
        
    @port2_statistic.setter
    def port2_statistic(self, port2_statistic: list[dict[str, list]]) -> None:
        self.__port2_statistic = port2_statistic
    
    @port1.setter
    def port1(self, port1: str) -> None:
        self.__port1 = port1

    @port2.setter
    def port2(self, port2: str) -> None:
        self.__port2 = port2
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @running.setter
    def running(self, running: bool) -> None:
        self.__running = running

    @booted.setter
    def booted(self, booted: bool) -> None:
        self.__booted = booted

    def disable_sending(self) -> None:
        self.__sending = False
    
    def enable_sending(self) -> None:
        self.__sending = True
    
    def __send_packet(self, packet: Packet, inter_from: str) -> None:
        
        if packet[Ether].dst in self.mac_table.entries:
            interface = self.mac_table.entries[packet[Ether].dst].port.name
            sendp(packet, iface=interface, verbose=False)
        else:
            for interface in self.working_interfaces:
                if interface != inter_from:
                    sendp(packet, iface=interface, verbose=False)

        log.info(f'Packet to {interface} is sent')

    def __packet_handler_without_sending(self, interface: str, packet: Packet) -> None:
        # log.info(f'Packet from {interface} is received')
        
        if not packet.getlayer(Ether):
            log.info('Packet is not Ethernet')
            return
        
        inter = self.interface_manager.get_interface(interface)
        
        len_before = len(self.mac_table.entries)

        self.mac_table.add_or_update_entry(packet[Ether].src, inter)
        self.mac_table.update()

        if len_before != len(self.mac_table.entries):
            self.__containers.websocket.mac_table = self.mac_table.entries

        json_packet_in = {"Ethernet2": "",
                       "IP": "",
                       "ARP": "",
                       "TCP": "",
                       "UDP": "",
                       "ICMP": "",
                       "HTTP": "",
                       "Total": ""}
        json_packet_out = {"Ethernet2": "",
                       "IP": "",
                       "ARP": "",
                       "TCP": "",
                       "UDP": "",
                       "ICMP": "",
                       "HTTP": "",
                       "Total": ""}

        total = 0
        if packet.haslayer(Ether):
            json_packet_in["Ethernet2"] = packet[Ether].type
            json_packet_out["Ethernet2"] = packet[Ether].type
            total += 1
        if packet.haslayer(IP):
            json_packet_in["IP"] = packet[IP].src
            json_packet_out["IP"] = packet[IP].dst
            total += 1
        if packet.haslayer(ARP):
            json_packet_in["ARP"] = packet[ARP].psrc
            json_packet_out["ARP"] = packet[ARP].pdst
            total += 1
        if packet.haslayer(TCP):
            json_packet_in["TCP"] = packet[TCP].sport
            json_packet_out["TCP"] = packet[TCP].dport
            total += 1
        if packet.haslayer(UDP):
            json_packet_in["UDP"] = packet[UDP].sport
            json_packet_out["UDP"] = packet[UDP].dport
            total += 1
        if packet.haslayer(ICMP):
            json_packet_in["ICMP"] = packet[ICMP].type
            json_packet_out["ICMP"] = packet[ICMP].type
            total += 1
        if packet.haslayer(HTTPRequest):
            json_packet_in["HTTP"] = packet[HTTPRequest].Method.decode()
            json_packet_out["HTTP"] = packet[HTTPRequest].Method.decode()
            total += 1
        json_packet_in["Total"] = total
        json_packet_out["Total"] = total

        if interface == self.port1:
            self.port1_statistic[0]['value1'].append(json_packet_in)
            self.port1_statistic[0]['value2'].append(json_packet_out)

            if len(self.port1_statistic[0]['value1']) > 50:
                self.__containers.websocket.port1_statistic = self.port1_statistic
                self.port1_statistic = [{"value1": [], "value2": []}]
        
        if interface == self.port2:
            self.port2_statistic[0]['value1'].append(json_packet_in)
            self.port2_statistic[0]['value2'].append(json_packet_out)

            if len(self.port2_statistic[0]['value1']) > 50:
                self.__containers.websocket.port2_statistic = self.port2_statistic
                self.port2_statistic = [{"value1": [], "value2": []}]
                
    def __packet_handler_with_sending(self, interface: str, packet: Packet) -> None:
        
        if not packet.getlayer(Ether):
            log.info('Packet is not Ethernet')
            return
        
        inter = self.interface_manager.get_interface(interface)
        
        len_before = len(self.mac_table.entries)

        self.mac_table.add_or_update_entry(packet[Ether].src, inter)
        self.mac_table.update()

        self.__send_packet(packet, interface)

        if len_before != len(self.mac_table.entries):
            self.__containers.websocket.mac_table = self.mac_table.entries

        json_packet_in = {"Ethernet2": "",
                       "IP": "",
                       "ARP": "",
                       "TCP": "",
                       "UDP": "",
                       "ICMP": "",
                       "HTTP": "",
                       "Total": ""}
        json_packet_out = {"Ethernet2": "",
                       "IP": "",
                       "ARP": "",
                       "TCP": "",
                       "UDP": "",
                       "ICMP": "",
                       "HTTP": "",
                       "Total": ""}

        total = 0
        if packet.haslayer(Ether):
            json_packet_in["Ethernet2"] = packet[Ether].type
            json_packet_out["Ethernet2"] = packet[Ether].type
            total += 1
        if packet.haslayer(IP):
            json_packet_in["IP"] = packet[IP].src
            json_packet_out["IP"] = packet[IP].dst
            total += 1
        if packet.haslayer(ARP):
            json_packet_in["ARP"] = packet[ARP].psrc
            json_packet_out["ARP"] = packet[ARP].pdst
            total += 1
        if packet.haslayer(TCP):
            json_packet_in["TCP"] = packet[TCP].sport
            json_packet_out["TCP"] = packet[TCP].dport
            total += 1
        if packet.haslayer(UDP):
            json_packet_in["UDP"] = packet[UDP].sport
            json_packet_out["UDP"] = packet[UDP].dport
            total += 1
        if packet.haslayer(ICMP):
            json_packet_in["ICMP"] = packet[ICMP].type
            json_packet_out["ICMP"] = packet[ICMP].type
            total += 1
        if packet.haslayer(HTTPRequest):
            json_packet_in["HTTP"] = packet[HTTPRequest].Method.decode()
            json_packet_out["HTTP"] = packet[HTTPRequest].Method.decode()
            total += 1
        json_packet_in["Total"] = total
        json_packet_out["Total"] = total

        if interface == self.port1:
            self.port1_statistic[0]['value1'].append(json_packet_in)
            self.port1_statistic[0]['value2'].append(json_packet_out)

            if len(self.port1_statistic[0]['value1']) > 50:
                self.__containers.websocket.port1_statistic = self.port1_statistic
                self.port1_statistic = [{"value1": [], "value2": []}]
        
        if interface == self.port2:
            self.port2_statistic[0]['value1'].append(json_packet_in)
            self.port2_statistic[0]['value2'].append(json_packet_out)

            if len(self.port2_statistic[0]['value1']) > 50:
                self.__containers.websocket.port2_statistic = self.port2_statistic
                self.port2_statistic = [{"value1": [], "value2": []}]

    def boot(self) -> None:
        if self.running or self.booted:
            raise SwitchIsActive
        self.booted = True
        self.interface_manager.boot()
        log.info('Switch is active')

    def choose_inter_to_run(self, interface_name: str) -> None:
        if self.running:
            raise SwitchIsActive
        if interface_name not in self.interface_manager.get_keys():
            raise InterfaceDoesNotExist
        if self.__sending:
            self.working_interfaces[interface_name] = Sniffer(interface_name, self.__packet_handler_with_sending)
        else:
            self.working_interfaces[interface_name] = Sniffer(interface_name, self.__packet_handler_without_sending)
        if self.port1 == None:
            self.port1 = interface_name
        elif self.port2 == None:
            self.port2 = interface_name
        self.interface_manager.update_interface_state(interface_name, 'up')
        log.info(f'Interface {interface_name} is added to working interfaces')

    def delete_inter_to_run(self, interface_name: str) -> None:
        if self.running:
            raise SwitchIsActive
        del self.working_interfaces[interface_name]
        self.interface_manager.update_interface_state(interface_name, 'down')

    def run(self) -> None:
        if self.running:
            raise SwitchIsActive
        if not self.booted:
            raise SwitchIsNotActive
        self.running = True
        for interface in self.working_interfaces.values():
            interface.start()
        log.info('Switch is running')

    def stop(self) -> None:
        if not self.running:
            raise SwitchIsNotActive
        for sniffer in self.working_interfaces.values():
            sniffer.stop()
        self.running = False
        for interface in self.working_interfaces.copy():
            self.delete_inter_to_run(interface)
        self.port1 = None
        self.port2 = None
        self.port1_statistic = [{"value1": [], "value2": []}]
        self.port2_statistic = [{"value1": [], "value2": []}]
        log.info('Switch is stopped')

    def stop_working_interface(self, interface_name: str) -> None:
        if not self.booted:
            raise SwitchIsNotActive
        self.working_interfaces[interface_name].stop()
        self.interface_manager.update_interface_state(interface_name, 'down')
        del self.working_interfaces[interface_name]

    def shutdown(self) -> None:
        if self.running:
            raise SwitchIsActive
        if not self.booted:
            raise SwitchIsNotActive
        self.booted = False
        self.interface_manager.shutdown()
        log.info('Switch is shutdown')
