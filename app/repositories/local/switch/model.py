from pydantic import BaseModel


class MacTableEntry(BaseModel):
    timer: int
    port: str
    last_seen: int


class MacTable(BaseModel):
    max_age: int
    entries: dict[str, MacTableEntry]


class Interface(BaseModel):
    name: str
    state: bool


class Switch(BaseModel):
    name: str
    description: str
    state: bool
    mac_table: MacTable
    interfaces: dict[str, Interface]
    