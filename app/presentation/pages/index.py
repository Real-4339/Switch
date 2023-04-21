from fastapi import Request
from fastapi import APIRouter
from app.di import containers
from fastapi.responses import HTMLResponse


index_page = APIRouter()

@index_page.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return containers.core.templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "interfaces": _,
            "port1": [{"value1": [], "value2": []}],
            "port2": [{"value1": [], "value2": []}],
            "macTable": [{}]
        }
    )