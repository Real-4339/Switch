from fastapi import FastAPI
from functools import cached_property
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


class CoreContainer:
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