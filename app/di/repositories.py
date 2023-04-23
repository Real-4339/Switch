from __future__ import annotations
import app.di.containers as di_containers

from functools import cached_property
from app.repositories.local.switch.repo import LocalSwitchRepo, InterfaceRepo, MacRepo

class Repositories:
    def __init__(self, containers: di_containers.Containers):
        self.__containers = containers
        
    @cached_property
    def local_switch(self):
        return LocalSwitchRepo(self.__containers)
    
    @cached_property
    def local_switch_interface(self):
        return InterfaceRepo(self.__containers)
    
    @cached_property
    def local_switch_mac(self):
        return MacRepo(self.__containers)