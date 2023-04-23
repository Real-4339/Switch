from pydantic import BaseModel


class MacTable(BaseModel):
    max_age: int


class Interface(BaseModel):
    name: str
    state: str


class LocalSwitch(BaseModel):
    name: str


class Switch(BaseModel):
    name: str
    description: str
    state: bool
    mac_table: MacTable
    interfaces: dict[str, Interface]
    