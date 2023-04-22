from fastapi import APIRouter
from app.di import containers


clears = APIRouter()

@clears.get('/clearMAC')
def clear_mac():
    '''Clear MAC address table'''
    #containers.core.repos.local_switch_mac.update('clear mac')


@clears.get('/clearStatistics')
def clear_statistics():
    '''Clear statistics'''
    #containers.core.repos.local_switch.update('clear statistics')