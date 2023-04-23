from functools import cached_property
from app.sources.local.switch import Switch


class Sources:
    @cached_property
    def local_switch(self) -> Switch:
        return Switch()

sources = Sources()