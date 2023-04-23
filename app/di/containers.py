from .core import CoreContainer
from .model import ModelContainer
from functools import cached_property
from .websocket import WebsocketContainer
from .sources import Sources

class Containers:
    @cached_property
    def core(self) -> CoreContainer:
        return CoreContainer(self)
    
    @cached_property
    def model(self) -> ModelContainer:
        return ModelContainer()
    
    @cached_property
    def websocket(self) -> WebsocketContainer:
        return WebsocketContainer(self.core)

    @cached_property
    def sources(self) -> Sources:
        return Sources(self)

containers = Containers()
