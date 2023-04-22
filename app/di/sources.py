from functools import cached_property


class Sources:
    @cached_property
    def local_switch(self):
        from app.sources.local.switch import Switch
        return Switch()