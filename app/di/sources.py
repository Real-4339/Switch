from functools import cached_property


class Sources:
    @cached_property
    def local_switch(self):
        from app.sources.local.switch import Switch
        return Switch()
    
    @cached_property
    def local_switch_interface(self):
        from app.sources.local.switch.inter_mg import InterfaceManager
        return InterfaceManager()
    
    @cached_property
    def local_switch_mac(self):
        from app.sources.local.switch.mac import MacTable
        return MacTable()
    
sources = Sources()