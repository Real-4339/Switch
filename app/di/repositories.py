from functools import cached_property
from app.repositories.local.switch.repo import LocalSwitchRepo


class Repositories:
    @cached_property
    def local_switch(self):
        return LocalSwitchRepo()