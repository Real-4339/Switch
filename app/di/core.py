import asyncio
from fastapi import FastAPI
from functools import cached_property
from .repositories import Repositories
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


class CoreContainer:
    def __init__(self, containers) -> None:
        self.__containers = containers
    
    @cached_property
    def loop(self) -> asyncio.AbstractEventLoop:
        return asyncio.get_event_loop()

    @cached_property
    def templates(self) -> Jinja2Templates:
        return Jinja2Templates(directory="app/presentation/resources/templates/html")
    
    @cached_property
    def static(self) -> str:
        return "app/presentation/resources/static"
    
    @cached_property
    def app(self) -> FastAPI:
        app = FastAPI()
        app.mount("/static", StaticFiles(directory=self.static), name="static")
        return app
    
    @cached_property
    def repos(self) -> Repositories:
        return Repositories(self.__containers)

# core = CoreContainer()
