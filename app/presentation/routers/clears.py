from fastapi import APIRouter
from app.di import containers


clears = APIRouter()

@clears.post('/clearMAC')
def clear_mac():
    '''Clear MAC address table'''
    containers.core.repos.local_switch_mac.delete()