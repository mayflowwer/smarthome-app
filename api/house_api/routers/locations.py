# api/location_router.py (или handlers/location.py)
from fastapi import APIRouter
import service.location_service as location_service
import models.location_model as models


router = APIRouter()

@router.get("/locations")
async def get_all_locations():
    """Получить все локации"""
    return await location_service.get_all_locations()

@router.get("/locations/{location_id}")
async def get_location_by_id(location_id: int):
    """Получить локацию по ID"""
    return await location_service.get_location_by_id(location_id)

@router.get("/houses/{house_id}")
async def get_locations_by_house(house_id: int):
    """Получить все локации для конкретного дома"""
    return await location_service.get_locations_by_house_id(house_id)

@router.post("/locations")
async def create_location(data: models.LocationCreate):
    """Создать новую локацию"""
    return await location_service.create_location(data)

@router.patch("/locations/{location_id}")
async def update_location(location_id: int, data: models.LocationUpdate):
    """Обновить локацию"""
    return await location_service.update_location(location_id, data)

@router.delete("/locations/{location_id}")
async def delete_location(location_id: int):
    """Удалить локацию"""
    return await location_service.delete_location(location_id)