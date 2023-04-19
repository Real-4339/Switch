from templates.yang_py import sw_interface


class InterfaceManager:
    def __init__(self):
        self.__interface_container = sw_interface.interface()

    def add_interface(self, interface_name: str) -> None:
        new_interface = self.__interface_container.interfaces.add(interface_name)
        new_interface.state = "down"

    def remove_interface(self, interface_name: str) -> None:
        try:
            self.__interface_container.interfaces.remove(interface_name)
        except AttributeError:
            raise ValueError("Interface does not exist")

    def get_interface(self, interface_name: str) -> sw_interface.interface.interfaces:
        try:
            return self.__interface_container.interfaces[interface_name]
        except AttributeError:
            raise ValueError("Interface does not exist")

    def get_interfaces(self):
        return self.__interface_container.interfaces
    
    def update_interface_name(self, old_name: str, new_name: str) -> None:
        if old_name not in self.__interface_container.interfaces:
            raise ValueError("Interface does not exist")
        self.__interface_container.interfaces[old_name].name = new_name

    def update_interface_state(self, interface_name: str, state: str) -> None:
        if state not in ["up", "down"]:
            raise ValueError("Invalid state")
        if interface_name not in self.__interface_container.interfaces:
            raise ValueError("Interface does not exist")
        self.__interface_container.interfaces[interface_name].state = state