from app.di import core
from .model import Switch

class LocalSwitchRepo:
    def __init__(self):
        self.local_switch = core.sources.local_switch

    def create(self, switch: Switch):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def delete(self, switch_id):
        raise NotImplementedError