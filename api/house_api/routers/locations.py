# api/location_router.py (или handlers/location.py)
from fastapi import APIRouter
import service.location_service as location_service
import validation_models.location_model as models


router = APIRouter(prefix="/locations")

@router.get("/")
async def get_all_locations():
    '''Get all locations'''
    return await location_service.get_all_locations()

@router.get("/{location_id}")
async def get_location_by_id(location_id: int):
    '''Get specified location by id'''
    return await location_service.get_location_by_id(location_id)

@router.post("/")
async def create_location(data: models.CreateLocation):
    '''Create location'''
    return await location_service.create_location(data)

@router.patch("/locations/{location_id}")
async def update_location(location_id: int, data: models.UpdateLocation):
    '''update location by id '''
    return await location_service.update_location(location_id, data)

@router.delete("/{location_id}")
async def delete_location(location_id: int):
    '''Delete location by id'''
    return await location_service.delete_location(location_id)
