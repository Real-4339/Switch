from functools import cached_property
from .core import CoreContainer


class Containers:
    @cached_property
    def core(self) -> CoreContainer:
        return CoreContainer()
    

containers = Containers()
