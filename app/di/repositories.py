from functools import cached_property
from app.repositories.local.switch.repo import LocalSwitchRepo, InterfaceRepo, MacRepo


class Repositories:
    @cached_property
    def local_switch(self):
        return LocalSwitchRepo()
    
    @cached_property
    def local_switch_interface(self):
        return InterfaceRepo()
    
    @cached_property
    def local_switch_mac(self):
        return MacRepo()