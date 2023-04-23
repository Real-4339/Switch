from .core import CoreContainer
from .model import ModelContainer
from functools import cached_property
from .websocket import WebsocketContainer


class Containers:
    @cached_property
    def core(self) -> CoreContainer:
        return CoreContainer()
    
    @cached_property
    def model(self) -> ModelContainer:
        return ModelContainer()
    
    @cached_property
    def websocket(self) -> WebsocketContainer:
        return WebsocketContainer()


containers = Containers()
