from .core import CoreContainer
from .model import ModelContainer
from functools import cached_property
from .repositories import Repositories


class Containers:
    @cached_property
    def core(self) -> CoreContainer:
        return CoreContainer()
    
    @cached_property
    def model(self) -> ModelContainer:
        return ModelContainer()
    
    @cached_property
    def repo(self) -> Repositories:
        return Repositories()
    

containers = Containers()
