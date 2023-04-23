from functools import cached_property
from app.sources.local.switch import Switch


class Sources:
    def __init__(self, containers) -> None:
        self.__containers = containers

    @cached_property
    def local_switch(self) -> Switch:
        return Switch(self.__containers)

