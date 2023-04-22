from uvicorn import run
from app.di import containers
from app.presentation.routers import root

app = containers.core.app
app.include_router(root)

# Events
@app.on_event("startup")
async def startup():
    containers.core.repos.local_switch.create()

@app.on_event("shutdown")
async def shutdown():
    containers.core.repos.local_switch.delete()

if __name__ == '__main__':
    run('app:app', host='127.0.0.1', port=8000, reload=True)
