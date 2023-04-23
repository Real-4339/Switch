from app.di import containers
from app.presentation.routers import root, events_router, \
                                    websock, clears, restconf_router, \
                                    timer_router

app = containers.core.app
app.include_router(root)
app.include_router(clears)
app.include_router(websock)
app.include_router(events_router)
app.include_router(restconf_router)
app.include_router(timer_router)

# Events
@app.on_event("startup")
async def startup():
    containers.core.repos.local_switch.create()

@app.on_event("shutdown")
async def shutdown():
    containers.core.repos.local_switch.delete()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
