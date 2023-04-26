from typing import Union
from fastapi import Body
from typing import Optional
from fastapi import APIRouter
from app.di import containers


events_router = APIRouter()

@events_router.post("/events", response_model=dict[str, Union[bool, str, list[str]]])
async def set_events(event: str = Body(..., embed=True), interface1: Optional[str] = Body(None), 
                     interface2: Optional[str] = Body(None)):
    if event == "start":

        containers.core.repos.local_switch.update("stop")

        containers.core.repos.local_switch.update(command="add interface", interfaces=[interface1, interface2])
        containers.core.repos.local_switch.update("run")

        return {"start": True}
    
    elif event == "stop":

        containers.core.repos.local_switch.update("stop")
        
        return {"stop": True}

    elif event == "refresh":

        new_interfaces = containers.core.repos.local_switch_interface.get()
        return {"interfaces": new_interfaces}

    elif event == "disable":
        res = containers.core.repos.local_switch.update("disable resending")
        
        if res is not None:
            return res
        
        return {"disable": True}
    
    elif event == "enable":
        res = containers.core.repos.local_switch.update("enable resending")
        if res is not None:
            return res
        
        return {"enable": True}