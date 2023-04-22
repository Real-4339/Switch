from app.di import containers
from app.presentation.routers import root
from app.presentation.websocket import websock

app = containers.core.app
app.include_router(root)
app.include_router(websock)

# Events
@app.on_event("startup")
async def startup():
    containers.core.repos.local_switch.create()

@app.on_event("shutdown")
async def shutdown():
    containers.core.repos.local_switch.delete()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("__main__:app", host='127.0.0.1', port=8000, reload=True)
