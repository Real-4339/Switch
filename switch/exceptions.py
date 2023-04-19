
class SwitchIsNotActive(Exception):
    def __init__(self):
        super().__init__('Switch is not active')

class SwitchIsActive(Exception):
    def __init__(self):
        super().__init__('Switch is active, cannot add/remove interface')

class InterfaceDoesNotExist(Exception):
    def __init__(self):
        super().__init__('Interface does not exist')

class InvalidState(Exception):
    def __init__(self):
        super().__init__('Invalid state')