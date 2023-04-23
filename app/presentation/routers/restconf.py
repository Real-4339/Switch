import pyangbind.lib.pybindJSON as pybindJSON

from app.di import containers
from fastapi import Depends, HTTPException, APIRouter, Body
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()
restconf_router = APIRouter()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    # function to check if the provided username and password are valid
    correct_username = 'myusername'
    correct_password = 'mypassword'
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return credentials.username

# -------------------------------------------- #

@restconf_router.get('/restconf/state')
async def restconf_state(username: str = Depends(get_current_username),
                         state: containers.model.interface = Body(...)):

    try:
        return containers.core.repos.local_switch_interface.get(command='get interface', interface=state.name)
    except Exception as e:
        return {"error": str(e)}
    
@restconf_router.put('/restconf/state')
async def restconf_state(username: str = Depends(get_current_username),
                            state: containers.model.interface = Body(...)):
        
        try:
            return containers.core.repos.local_switch_interface.update(command='update state', interface=state.name, state=state.state)
        except Exception as e:
            return {"error": str(e)}

# -------------------------------------------- #
    
@restconf_router.get('/restconf/interface_name')
async def restconf_name(username: str = Depends(get_current_username),
                         interface: containers.model.interface = Body(...)):
    
    if interface.state == 'up':
        listik = containers.core.repos.local_switch_interface.get(command='up')
        dictionary = {}
        for i in listik:
            dictionary[i] = 'up'
        return dictionary

    elif interface.state == 'down':
        listik = containers.core.repos.local_switch_interface.get(command='down')
        dictionary = {}
        for i in listik:
            dictionary[i] = 'down'
        return dictionary
    
    elif interface.state == 'all':
        return containers.core.repos.local_switch_interface.get(command='all')
    
@restconf_router.put('/restconf/interface_name')
async def restconf_name(username: str = Depends(get_current_username),
                         interface: containers.model.interface_name = Body(...)):

    res = containers.core.repos.local_switch_interface.update(command='update name', interface=interface.interface, name=interface.name)
    print(res)
    return res
    
# -------------------------------------------- #

@restconf_router.get('/restconf/hostname')
async def restconf_hostname(username: str = Depends(get_current_username),
                         hostname: containers.model.local_switch = Body(...)):
    
    print(hostname)
    return containers.core.repos.local_switch.get(command='name')

@restconf_router.put('/restconf/hostname')
async def restconf_hostname(username: str = Depends(get_current_username),
                         hostname: containers.model.local_switch = Body(...)):
    
    return {'new hostname': containers.core.repos.local_switch.update(command='name', name=hostname.name)}

# -------------------------------------------- #

@restconf_router.get('/restconf/mac_timer')
async def restconf_mac_timer(username: str = Depends(get_current_username),
                             mac: containers.model.mac_table = Body(...)):
    
    return {'timer' : containers.core.repos.local_switch_mac.get()}

@restconf_router.put('/restconf/mac_timer')
async def restconf_mac_timer(username: str = Depends(get_current_username),
                             mac: containers.model.mac_table = Body(...)):
    
    return {'new timer' : containers.core.repos.local_switch_mac.update(timer=mac.max_age)}