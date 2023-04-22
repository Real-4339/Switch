from .core import CoreContainer
from .model import ModelContainer
from functools import cached_property


class Containers:
    @cached_property
    def core(self) -> CoreContainer:
        return CoreContainer()
    
    @cached_property
    def model(self) -> ModelContainer:
        return ModelContainer()
    

containers = Containers()
