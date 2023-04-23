from app.di import containers
from fastapi import APIRouter, Body


timer_router = APIRouter()

@timer_router.post('/timer', response_model=dict[str, bool])
async def set_timer(timer: int = Body(..., embed=True)):
    try:
        set_timer.lock
    except AttributeError:
        set_timer.lock = False
    
    if set_timer.lock == False:
        set_timer.lock = True
        
        containers.core.repos.local_switch_mac.update(timer=timer)
        
        return {"timer": False}
    else:
        return {"timer": True}