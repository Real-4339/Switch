class LocalSwitch:
    def __init__(self) -> None:
        self.controlls = self.Controlls()
        self.configurate = self.Configurate()
        self.mac_table = self.MacTable()
    
    def get_status(self) -> dict:
        return {
            "metadata" : ...
        }
    
    class Controlls:
        def __init__(self) -> None:
            pass
        
        def on(self) -> None:
            pass
        
        def off(self) -> None:
            pass
        
        def toggle(self) -> None:
            pass
    
    class Configurate:
        def __init__(self) -> None:
            pass
        
        def get(self) -> dict:
            return {
                "metadata" : ...
            }
        
        def set(self, config: dict) -> None:
            pass
            
        def reset(self) -> None:
            pass
    
    class MacTable:
        def __init__(self) -> None:
            pass
        
        def get(self) -> dict:
            return {
                "metadata" : ...
            }
        
        def set(self, config: dict) -> None:
            pass
            
        def reset(self) -> None:
            pass


__all__ = [
    'LocalSwitch',
]